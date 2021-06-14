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
    """ Assign ref image to product
    """
    try:
        product_id = event["pathParameters"]['product_id']
        reference_image_id = event["pathParameters"]['reference_image_id']
        body = json.loads(event['body'])
        gcs_uri = body["gcs_uri"]
        client = vision.ProductSearchClient()
        product_path = client.product_path(project=project_id, location=location, product=product_id)
        reference_image = vision.types.ReferenceImage(uri=gcs_uri)
        image = client.create_reference_image(parent=product_path, reference_image=reference_image,
                                              reference_image_id=reference_image_id)
        result = {"Reference image name": image.name,
                  "Reference image uri": image.uri}
    except Exception as err:
        raise {"statusCode": 500, "body": json.dumps(str(err))}
    return {"statusCode": 200, "body": json.dumps(result)}
