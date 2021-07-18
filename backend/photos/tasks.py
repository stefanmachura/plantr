from celery import shared_task

import logging
import boto3
from botocore.exceptions import ClientError

from photos.models import Photo


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client("s3", region_name="eu-west-1")
    s3_client.upload_file(
        file_name, bucket, object_name, ExtraArgs={"ACL": "public-read"}
    )
    file_url = "%s/%s/%s" % (s3_client.meta.endpoint_url, bucket, object_name)
    return file_url


@shared_task
def upload_photo_to_s3(pk):
    print(f"started task, pk is {pk}", flush=True)
    photo = Photo.objects.get(pk=pk)
    fname = photo.temp_file.name.split("/")[-1]
    if fname == "":
        return "no photo uploaded"
    try:
        url = upload_file(f"uploads/{fname}", "shared-stfn")
    except ClientError as e:
        return e
    photo.temp_file = None
    photo.s3_url = url
    photo.save()
    return url
