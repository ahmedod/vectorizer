# landmark_detection

export GOOGLE_APPLICATION_CREDENTIALS=/landmark-project-267511-47fa80d3f8bf.json
# Upload image to cloud storage

gsutil cp landmark.jpg gs://landmark-images-buckets/landmark.jpg
# This step is unnecessary with default permissions, but for completeness,
# explicitly give the service account access to the image. This email can
# be found by running:
# `grep client_email /path/to/your-project-credentials.json`
gsutil acl ch -u <dev-landmark-project@landmark-project-267511.iam.gserviceaccount.com>:R \
    gs://landmark-images-buckets/landmark.jpg

# Run sample
./detect_landmark.py gs://landmark-images-buckets/landmark.jpg


# Deployement
gcloud functions deploy ocr-extract --runtime python37 --trigger-http --entry-point process_image --project landmark-project-267511


