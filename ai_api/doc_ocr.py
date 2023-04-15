from google.api_core.client_options import ClientOptions
from google.cloud import documentai_v1 as documentai
from dotenv import load_dotenv
import google.auth
import google.auth.impersonated_credentials
import os

load_dotenv()

LOCATION = os.environ["LOCATION"]
PROJECT_ID = os.environ["PROJECT_ID"]
PROCESSOR_ID = os.environ["PROCESSOR_ID"]
MIME_TYPE = 'application/pdf'

def extract_text(image_content):

    docai_client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
    )

    RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=image_content, mime_type=MIME_TYPE)

    # Configure the process request
    request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

    # Use the Document AI client to process the sample form
    result = docai_client.process_document(request=request)

    return result.document

if __name__ == "__main__":
    FILE_PATH = './test_pdf/pythagoras.pdf'

    # Read the file into memory
    with open(FILE_PATH, "rb") as image:
        image_content = image.read()

    document_object = extract_text(image_content)

    print("Document processing complete.")
    # print(f"Text: {document_object.text}")
    print(len(document_object.text))
