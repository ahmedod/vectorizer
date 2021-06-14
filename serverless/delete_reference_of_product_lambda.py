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
    """ list all productset
    """
    try:
        product_id = event["pathParameters"]['product_id']
        reference_image_id = event["pathParameters"]['reference_image_id']
        client = vision.ProductSearchClient()
        reference_image_path = client.reference_image_path(project=project_id, location=location, product=product_id,
                                                           reference_image=reference_image_id)
        client.delete_reference_image(name=reference_image_path)
        message = "Reference image deleted from product."
    except Exception as err:
        raise {"statusCode": 500, "body": json.dumps(str(err))}
    return {"statusCode": 200, "body": json.dumps(message)}
