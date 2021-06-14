import os
import json
from google.cloud import vision
from google.cloud.vision import types


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")


def lambda_handler(event, context):
    client = vision.ProductSearchClient()
    body = json.loads(event['body'])
    gcs_uri = body["gcs_uri"]
    
    location_path = client.location_path(project=project_id, location=location)
    gcs_source = vision.types.ImportProductSetsGcsSource(csv_file_uri=gcs_uri)
    input_config = vision.types.ImportProductSetsInputConfig(gcs_source=gcs_source)

    # Import the product sets from the input URI.
    response = client.import_product_sets(parent=location_path, input_config=input_config)


    # synchronous check of operation status
    result = response.result()
    return {"statusCode": 200, "body": json.dumps(result)}
