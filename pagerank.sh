cd ./pagerank
scrapy crawl ranker -a url="$1" -O "../output.json" --nolog
cd ..
python calc_rank.py
