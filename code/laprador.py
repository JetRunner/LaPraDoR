import numpy as np
import logging
import pathlib, os
import torch
import pickle
import gc
import sys

from beir import util, LoggingHandler
from beir.retrieval import models
from beir.datasets.data_loader import GenericDataLoader
from beir.retrieval.evaluation import EvaluateRetrieval
from beir.retrieval.search.dense import DenseRetrievalExactSearch as DRES


model = DRES(models.SentenceBERT("canwenxu/laprador"), batch_size=512)
retriever = EvaluateRetrieval(model, score_function="cos_sim")


dataset = sys.argv[1]
split = sys.argv[2]

url = "https://public.ukp.informatik.tu-darmstadt.de/thakur/BEIR/datasets/{}.zip".format(dataset)
data_path = util.download_and_unzip(url, "datasets")
corpus, queries, qrels = GenericDataLoader(data_folder=data_path).load(split=split)

bm25_result = pickle.load(open("BM25-result/{}.pkl".format(dataset),"rb"))
corpus_ids = set([y[0] for x in bm25_result for y in sorted(bm25_result[x].items(), key = lambda kv:-kv[1])[:100]])
corpus = {x: corpus[x] for x in corpus_ids}

results = retriever.retrieve(corpus, queries, bm25_result = bm25_result)

ndcg, _map, recall, precision = retriever.evaluate(qrels, bm25_result, retriever.k_values)
print("SciFact (BM25)",round(ndcg["NDCG@10"],3))
ndcg, _map, recall, precision = retriever.evaluate(qrels, results, retriever.k_values)
print("SciFact (BM25+Dense)",round(ndcg["NDCG@10"],3))

