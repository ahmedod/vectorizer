""" App module"""
# set the env path
import os
from dotenv import load_dotenv
import os
from pathlib import Path

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
PRODUCTS_LOCATION = os.getenv("PRODUCTS_LOCATION")


