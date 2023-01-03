import pymongo
import pandas as pd
import json
# Provide the mo8ngodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"


if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #convert dataframe into json format so that we can dump our record into mongodb
    df.reset_index(drop=True, inplace=True)

    json_record=list(json.loads(df.T.to_json()).values()) #convert record to json format
    print(json_record[0])

   #insert converted rows to json format
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)