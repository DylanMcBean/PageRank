# page_rank

just a simple few scripts that you can run that will give back the page rank of all the pages on a website

## Requirements
```
scrapy
numpy
```
run `pip install -r requirements.txt` to install them

### How to run

just clone the repo and unzip. then in the main folder call the pagerank.sh file with a website
like this

```
./pagerank.sh "http://toscrape.com"
```

this will scrape the website toscrape.com and give back the resulting page ranking for it

```
Calculating Page Rank
Getting Unique Links
Number of Unique Links found: 1639
Number of Website Pages: 1587
Creating Adjacency Matrix
Converting Adjacency Matrix to probabilities
Transposing Adjacency Matrix
Matrix Mult Iteration: 141
Top 25 Links

 PAGE RANK |                                                  SITE                                                   | RANK SCORE
     1     | http://books.toscrape.com/index.html                                                                    | 0.7324421758942409
     2     | http://books.toscrape.com/catalogue/category/books_1/index.html                                         | 0.4064413807410632
     3     | http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html                                | 0.13816165137261371
     4     | http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html                                   | 0.11000221103544246
     5     | http://books.toscrape.com/catalogue/category/books/poetry_23/index.html                                 | 0.1051367618840453
     6     | http://books.toscrape.com/catalogue/soumission_998/index.html                                           | 0.0949508419102855
     7     | http://books.toscrape.com/catalogue/sharp-objects_997/index.html                                        | 0.08620705240207238
     8     | http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html                 | 0.08084140706899201
     9     | http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html                      | 0.0779473218874319
    10     | http://books.toscrape.com/catalogue/the-requiem-red_995/index.html                                      | 0.07755159700769004
    11     | http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html   | 0.07554318718468833
    12     | http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-femin... | 0.07321832812024856
    13     | http://books.toscrape.com/catalogue/category/books/default_15/index.html                                | 0.07185974660766002
    14     | http://books.toscrape.com/catalogue/category/books/fiction_10/index.html                                | 0.07118468293707227
    15     | http://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gol... | 0.07063044956862086
    16     | http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html                            | 0.06863824797441695
    17     | http://books.toscrape.com/catalogue/the-black-maria_991/index.html                                      | 0.06847504951330492
    18     | http://books.toscrape.com/catalogue/category/books/mystery_3/index.html                                 | 0.06824978455217705
    19     | http://books.toscrape.com/catalogue/category/books/history_32/index.html                                | 0.0651640596099434
    20     | http://books.toscrape.com/catalogue/starving-hearts-triangular-trade-trilogy-1_990/index.html           | 0.06477489075151047
    21     | http://books.toscrape.com/catalogue/category/books/music_14/index.html                                  | 0.06270138793675875
    22     | http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html                                 | 0.06233524396778676
    23     | http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html                          | 0.06221179121043262
    24     | http://books.toscrape.com/catalogue/category/books/business_35/index.html                               | 0.061615988681410216
    25     | http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html                        | 0.05998985894324003

Page rank written to page_rank.txt

```
