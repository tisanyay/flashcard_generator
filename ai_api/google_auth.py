import google.auth
import google.auth.impersonated_credentials
from google.cloud import storage

creds, pid = google.auth.default()
print(f"Obtained default credentials for the project {pid}")
tcreds = google.auth.impersonated_credentials.Credentials(
    source_credentials=creds,
    target_principal="github-resource-access@flashcard-generator-383608.iam.gserviceaccount.com"
)
