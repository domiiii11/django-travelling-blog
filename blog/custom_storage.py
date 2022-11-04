from storages.backends.s3boto3 import S3Boto3Storage
import boto3
import environ

class MediaStorage(S3Boto3Storage):
    bucket_name = 'django-blog-bucket112'
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object
    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """
    env = environ.Env()
    environ.Env.read_env()
    AWS_S3_ACCESS_KEY_ID = env("AWS_S3_ACCESS_KEY_ID")
    print(AWS_S3_ACCESS_KEY_ID)
    AWS_S3_SECRET_ACCESS_KEY = env("AWS_S3_SECRET_ACCESS_KEY")
    print(AWS_S3_SECRET_ACCESS_KEY)
    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3', aws_access_key_id=AWS_S3_ACCESS_KEY_ID, aws_secret_access_key=AWS_S3_SECRET_ACCESS_KEY)
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response