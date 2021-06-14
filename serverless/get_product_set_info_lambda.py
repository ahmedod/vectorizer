import os
import json
from google.cloud import vision
from google.cloud.vision import types


class Exception(BaseException):
    pass


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")


def lambda_handler(event, context):
    """ create a productset
    """
    try:
        product_set_id = event["pathParameters"]['product_set_id']
        client = vision.ProductSearchClient()
        product_set_path = client.product_set_path(project=project_id, location=location, product_set=product_set_id)
        product_set = client.get_product_set(name=product_set_path)
        result = {"Product set name": str(product_set.name),
                  "Product set id": str(product_set.name.split('/')[-1]),
                  "Product set display name": str(product_set.display_name),
                  "Product set index time: seconds": str(product_set.index_time.seconds),
                  "Product set index time: nanos": str(product_set.index_time.nanos)}
    except Exception as err:
        raise {"statusCode": 500, "body": json.dumps(str(err))}
    return {"statusCode": 200, "body": json.dumps(result)}
