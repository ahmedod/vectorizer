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
        client = vision.ProductSearchClient()
        product_path = client.product_path(project=project_id, location=location, product=product_id)
        reference_images = client.list_reference_images(parent=product_path)
        results = []
        for image in reference_images:
            results.append({"Reference image name": image.name,
                            "Reference image id": image.name.split('/')[-1],
                            "Reference image uri": image.uri})
    except Exception as err:
        raise {"statusCode": 500, "body": json.dumps(str(err))}
    return {"statusCode": 200, "body": json.dumps(results)}
