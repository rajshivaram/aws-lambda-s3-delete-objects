import json
import boto3
from pprint import pprint

s3_client = boto3.client("s3")
s3_bucket = "SPECIFY_BUCKET_NAME"
s3_prefix = "IMAGES/"


def lambda_handler(event,context):

    # List all files in the folder
    response = s3_client.list_objects_v2(Bucket=s3_bucket, Prefix=s3_prefix)
    files_in_folder = response["Contents"]
    files_to_delete = []

    # Create Key array to pass to delete_objects function

    for f in files_in_folder:
        files_to_delete.append({"Key": f["Key"]})

    # This will delete all files in a folder
    response = s3_client.delete_objects(
        Bucket=s3_bucket, Delete={"Objects": files_to_delete}
    )
    pprint(response)
