import shutil
import sys
import json
import boto3
import os
from minio import Minio

new_minio = Minio(
    "137.226.188.114:32763",
    secure=False,
    access_key="databatt",
    secret_key="databatt",
)


def transfer_data(bucket_name):
    rr = new_minio.bucket_exists(bucket_name)
    if rr:
        print(f"Bucket {bucket_name} already exists")
    else:
        new_minio.make_bucket(bucket_name)
        print(f"Bucket {bucket_name} Created!!")
    data = [
        {"Reference": "WH/MO/00005", "Duration": 30, "Company": "New York", "Scheduled Date": "21/12/2022",
         "Product": "SG201-PiCase", "Quantity": 450, "State": "In Progress"},
        {"Reference": "WH/MO/00006", "Duration": 25, "Company": "San Francisco", "Scheduled Date": "12/06/2022",
         "Product": "SG201-PiCase", "Quantity": 450, "State": "Confirmed"},
        {"Reference": "WH/MO/00001", "Duration": 35, "Company": "Los Angeles", "Scheduled Date": "12/12/2022",
         "Product": "SG006-Pinocchio", "Quantity": 450, "State": "Confirmed"},
        {"Reference": "WH/MO/00002", "Duration": 45, "Company": "Los Angeles", "Scheduled Date": "11/12/2022",
         "Product": "SG006-Pinocchio", "Quantity": 450, "State": "In Progress"},
        {"Reference": "WH/MO/00003", "Duration": 35, "Company": "Los Angeles", "Scheduled Date": "12/11/2022",
         "Product": "SG201-PiCase", "Quantity": 450, "State": "Confirmed"}
    ]
    directory_name = './tmp'
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    local_dir_name = directory_name + '/' + 'data.json'

    with open(local_dir_name, 'w') as file:
        json.dump(data, file)

    try:
        new_minio.fput_object(bucket_name, 'data.json', local_dir_name)
        print("Data uploaded successfully to Minio.")
    except Exception as e:
        print(f"Error uploading data: {e}")

    shutil.rmtree(directory_name)
    directory_name = './tmp'
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    try:
        new_minio.fget_object(bucket_name, 'data.json', local_dir_name)
        print("Data Downloaded!!")
    except Exception as e:
        print(f"Error uploading data: {e}")

    with open(local_dir_name, 'r') as file:
        downloaded_data = json.load(file)

    for record in downloaded_data:
        print(record)

    shutil.rmtree(directory_name)


def get_record(bucket_name):
    try:
        response = new_minio.get_object(bucket_name, 'data.json')
        print("Data Downloaded!!")
    except Exception as e:
        print(f"Error uploading data: {e}")

    return response.data




if __name__ == "__main__":
    bucketName = "model-45"
    # comment the below line if the data is not be transfered
    # transfer_data(bucketName)
    r = get_record(bucketName)
    print(r)
    # For removing data from a bucket remove the comment # from the below line
