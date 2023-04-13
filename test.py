gcloud iam service-accounts add-iam-policy-binding "githubsecret@flashcard-generator-383608.iam.gserviceaccount.com" \
  --project="flashcard-generator-383608" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/189439450845/locations/global/workloadIdentityPools/flashcardgeneratorkeys/attribute.repository/${REPO}"

principalSet://iam.googleapis.com/projects/189439450845/locations/global/workloadIdentityPools/flashcardgeneratorkeys/*

