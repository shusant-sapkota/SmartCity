# import dash
# from dash import dcc,html
# import plotly.express as px
import io
import os
from io import StringIO
import boto3
from dotenv import load_dotenv, find_dotenv
import s3fs as fs
import pandas as pd

load_dotenv(find_dotenv())

bucket = 'ss-spark-streaming-data'

s3_connection = boto3.client(
    's3',
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key= os.getenv('AWS_SECRET_KEY'),
    aws_session_token = os.getenv('AWS_SECRET_TOKEN')
)

def get_data_paths_from_s3(file_prefix):
    response = s3_connection.list_objects_v2(
        Bucket = bucket,
        Prefix  = file_prefix
    )

    data_files_list = []

    if 'Contents' in response:
        for obj in response['Contents']:
            data_files_list.append(obj['Key'])
        return data_files_list
    else:
        print('No data in the mentioned folder of the bucket')

vehicle_data_files_list = get_data_paths_from_s3('data/vehicle_data/part')
gps_data_files_list = get_data_paths_from_s3('data/gps_data/part')
emergency_data_files_list = get_data_paths_from_s3('data/emergency_data/part')
traffic_data_files_list = get_data_paths_from_s3('data/traffic_data/part')
weather_data_files_list = get_data_paths_from_s3('data/weather_data/part')

# print(vehicle_data_files_lits)
# print(len(vehicle_data_files_lits))

#data/vehicle_data/part-00000-153709e5-e941-4567-a4dd-69d14242b440-c000.snappy.parquet

def get_data_from_s3(bucket, list_of_data_paths):
    fun_df = pd.DataFrame()
    for data_path in list_of_data_paths:
        response = s3_connection.get_object(
            Bucket=bucket,
            Key=data_path
        )

        parquet_data = response['Body'].read()
        temp_df = pd.read_parquet(io.BytesIO(parquet_data))

        fun_df = pd.concat([fun_df, temp_df], axis=0, ignore_index=True)
    return fun_df


vehicle_df = get_data_from_s3(bucket, vehicle_data_files_list)
emergency_df = get_data_from_s3(bucket, emergency_data_files_list)
weather_df = get_data_from_s3(bucket, weather_data_files_list)
traffic_df = get_data_from_s3(bucket, traffic_data_files_list)
gps_df = get_data_from_s3(bucket, gps_data_files_list)


print(vehicle_df.shape)
print(emergency_df.shape)
print(weather_df.shape)
print(traffic_df.shape)
print(gps_df.shape)