# Big data for youtube data:
## Understand below questions youtube's adv data: 
1. How to categorize videos based on comments and statistics?
2. What factors affect the popularity of a video?

# Set-up steps:
Download dataset from :
    https://www.kaggle.com/datasets/datasnaek/youtube-new?resource=download
1. Create AWS Account.
2. Create IAM account for the project.
3. Install and configure aws cli
4. Create s3 bucket
5. Move data to s3
    Check the s3-script.sh file
6. Create a Glue Crawler
7. Createa role to access s3 and GlueService role
8. Run the Glue Crawler by pointing it to the raw S3 bucket that contains all .json data.
9. Running the crawler on raw json data and build a catalog on top of it. Creates a table as well on the database. There will be 3 columns :
    ``` "kind"
    "etag"
    "items"```
    These columns are from the .json files.
10. Then view data on  the table and Athena opens up but with the below error:
    ```No output location provided```
11. Click on settings on the query editor, and provide a new s3 bucket to store the results. Re-run the query.
12. This would still error out with:
    ```Row is not a valid json object```

13. This references to the json key "items": [""]
    Since this contains multiple keys, we need to do preprocessing on items to extract data from items and store it into a catalog and then use crawler to access this data.

24. Convert JSON -> PARQUET -> Store parquet in a new glue catalog, new table and Qury the Data.
25. Write a lambda function : lambda-convert_json-parquet
26. Ensure you run this labda with a Python 3.8 runtime version otherwise it will error out saying "Module not found ciff"
27. Add layer AWSSDKPandas-Python38,AWS-AppConfig-Extension
28. Increase timeout of landba to 3 minutes, memory to 1024
29. Add the policy "AWSGlueServiceRole"  to the role used by lambda service to create table on glue.
30. Create the new cleansed-db catalog on Glue and run the lamdba on a 'Test' s3-put module




