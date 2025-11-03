"""
This is a script to take a backup from local to AWS S3
boto3 -> used to do AWS tasks using Python
"""

import boto3

region = "ap-south-1"
bucket_name = "python-for-devops-dayith123"

s3 = boto3.resource('s3', region_name=region)

def show_buckets(s3):
  for bucket in s3.buckets.all():
      print(bucket.name)
      
def create_bucket(s3):
    s3.create_bucket(Bucket=bucket_name,
                     CreateBucketConfiguration={
                     'LocationConstraint': region,
    },)
    print("Bucket created successfully")
    
def upload_backup(s3,file_name,bucket_name,key_name):
    """
       Upload a given backup file path to a given s3 bucket
       with a new key name
    """
    data = open(file_name, 'rb') #Read binary mode
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully")    
#create_bucket(s3) 
#show_buckets(s3)
file_name="/Users/Admin/Desktop/Python/python-workshop-practice/backups/backup_2025-11-03.tar.gz"
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz")