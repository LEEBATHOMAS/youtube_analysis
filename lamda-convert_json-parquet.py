import awswrangler as wr   #library used to access AWS
import pandas as pd
import urllib.pandas        
import os


#default values

os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name  = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']





def lamdba_handler(event,context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        #extract data frame from the bucket and key in the event
        df_raw = wr.s3.read_json('s3://{}}/{}}'.format(bucket,key))

        #extract the columns from file and flatten it out to table - columns
        df_step1 = pd.json_normalize(df_raw['items'])

        #write to S3
        wr_response = wr.s3.to_parquet(
                                        df=df_step1,path=os_input_s3_cleansed_layer,
                                        dataset=True,
                                        database=os_input_glue_catalog_db_name,
                                        table=os_input_glue_catalog_table_name,
                                        mode=os_input_write_data_operation
                                        )
        

        return wr_response
    
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure dataset exists in bucket'.format(key,bucket))
        raise e

