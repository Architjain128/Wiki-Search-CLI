# How to run
Clone this repo and run following commands  
```
    > cd code
    > pip3 install -r requirement.txt
```
```
    > python3
        >> import nltk
        >> nltk.download('stopwords')
```
## For Indexer
```
    > bash index.sh <dump_file_path> <invert_folder_path> <stat_file_path>
```
## For Search
```
    > bash search.sh <invert_folder_path> <query_string>
```
## Report
```
    Location :  ./code/final_report.txt
```
