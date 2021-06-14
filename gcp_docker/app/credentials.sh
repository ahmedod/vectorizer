#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS=key.json
export MONGODB_USERNAME=flaskuser
export MONGODB_PASSWORD=dbc_wess
export MONGODB_DATABASE=flaskdb
export MONGODB_HOSTNAME=mongodb
export APP_ENV=prod
export APP_DEBUG=True
export APP_PORT=5000
export GCP_PROJECT=landmark-project-267511

echo "gcloud auth activate-service-account dev-landmark-project@landmark-project-267511.iam.gserviceaccount.com --key-file=key.json --project=landmark-project-267511"
