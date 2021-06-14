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
        client = vision.ProductSearchClient()
        location_path = client.location_path(project=project_id, location=location)
        product_sets = client.list_product_sets(parent=location_path)
        results = []
        for product_set in product_sets:
            results.append({"Product set name": str(product_set.name),
                            "Product set id": str(product_set.name.split('/')[-1]),
                            "Product set display name": str(product_set.display_name),
                            "Product set index time: seconds": str(product_set.index_time.seconds),
                            "Product set index time: nanos": str(product_set.index_time.nanos)})
    except Exception as err:
        raise {"statusCode": 500, "body": json.dumps(str(err))}
    return {"statusCode": 200, "body": json.dumps(results)}
