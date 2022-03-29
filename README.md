<img width="1204" alt="LaPraDoR promotion" src="https://user-images.githubusercontent.com/22514219/160527465-049cdc62-ce23-46e3-97fd-ad5f543e093c.png">

Code and pretrained models for Findings of ACL 2022 paper [LaPraDoR: Unsupervised Pretrained Dense Retriever for Zero-Shot Text Retrieval](https://arxiv.org/abs/2203.06169).

In this repo, we provide codes for reproducing experiments on BEIR dataset in the zero-shot setting of the paper. For fine-tuning, please follow the instructions in [BEIR repo](https://github.com/beir-cellar/beir).

Note that due to copyright restrictions, some datasets are not available.

### Installation

```bash
git clone https://github.com/benchmarkir/beir.git
cp code/exact_search.py beir/beir/retrieval/search/dense/exact_search.py
cp code/bm25.py beir
cp code/laprador.py beir
cd beir
pip install -e .
pip install tensorflow==2.5.0
```

### Download pre-processed BM25 index
```bash
# cd ./beir
wget https://github.com/JetRunner/LaPraDoR/releases/download/v0.1/BM25-result.zip
unzip BM25-result.zip
```

### Retrieve with LaPraDoR

```bash
# Please refer to https://github.com/beir-cellar/beir#beers-available-datasets for dataset name and split
dataset=trec-covid
split=test
python laprador.py $dataset $split
```

### Use your own dataset (requires Elasticsearch)
To use your own dataset, please process the data to the same format as [BEIR](https://github.com/beir-cellar/beir#beers-available-datasets) and then index the dataset following `bm25.py`. You will need Elasticsearch to index the corpus.

#### Install Elasticsearch

##### Installation

Following [this link](https://linuxize.com/post/how-to-install-elasticsearch-on-ubuntu-18-04/) to download Elasticsearch. Here, we use Ubuntu 18.04 as an example.

```bash
sudo apt update
sudo apt install apt-transport-https
sudo mkdir -p /usr/share/man/man1
sudo apt install openjdk-8-jdk
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo sh -c 'echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" > /etc/apt/sources.list.d/elastic-7.x.list'
sudo apt update
sudo apt install elasticsearch
```

##### Start Elasticsearch

```bash
sudo systemctl enable elasticsearch.service # or sudo service elasticsearch enable
sudo systemctl start elasticsearch.service # or sudo service elasticsearch start

# You can verify that Elasticsearch is running by sending an HTTP request to port 9200 on localhost with the following curl command:
curl -X GET "localhost:9200/"
```

### Citation
```bibtex
@inproceedings{xu2022laprador,
    title={{LaPraDoR}: Unsupervised Pretrained Dense Retriever for Zero-Shot Text Retrieval},
    author={Canwen Xu and Daya Guo and Nan Duan and Julian McAuley},
    booktitle={{ACL} 2022 (Findings)},
    year={2022}
}
```
