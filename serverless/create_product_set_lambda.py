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
        product_set_id = event["queryStringParameters"]['product_id']
        product_set_name = event["queryStringParameters"]['product_name']
        client = vision.ProductSearchClient()
        location_path = client.location_path(project=project_id, location=location)
        # Create a product set with the product set specification in the region.
        product_set = vision.types.ProductSet(display_name=product_set_name)
        # The response is the product set with `name` populated.
        response = client.create_product_set(parent=location_path, product_set=product_set,
                                             product_set_id=product_set_id)
    except Exception as err:
        raise {"statusCode": 500, "body": json.dumps(str(err))}
    return {"statusCode": 200, "body": json.dumps(str(response))}
