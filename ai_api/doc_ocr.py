from google.api_core.client_options import ClientOptions
from google.cloud import documentai_v1 as documentai
from dotenv import load_dotenv
import os

load_dotenv()

LOCATION = os.environ["LOCATION"]
PROJECT_ID = os.environ["PROJECT_ID"]
PROCESSOR_ID = os.environ["PROCESSOR_ID"]
MIME_TYPE = 'application/pdf'

credential_path = './ai_api/clientLibraryConfig-github.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def extract_text(image_content):

    docai_client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
    )

    RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

    # Read the file into memory
    # with open(FILE_PATH, "rb") as image:
        # image_content = image.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=image_content, mime_type=MIME_TYPE)

    # Configure the process request
    request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

    # Use the Document AI client to process the sample form
    result = docai_client.process_document(request=request)

    return result.document

if __name__ == "__main__":
    # test_pdf_path = './test_pdf/pythagoras.pdf'

    # with open(test_pdf_path, "rb") as image:
        # image_content = image.read()
    
    # print(extract_text(image_content).text)

    FILE_PATH = './test_pdf/pythagoras.pdf'

    # Instantiates a client
    docai_client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
    )

    # The full resource name of the processor, e.g.:
    # projects/project-id/locations/location/processor/processor-id
    # You must create new processors in the Cloud Console first
    RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

    # Read the file into memory
    with open(FILE_PATH, "rb") as image:
        image_content = image.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=image_content, mime_type=MIME_TYPE)

    # Configure the process request
    request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

    # Use the Document AI client to process the sample form
    result = docai_client.process_document(request=request)

    document_object = result.document

    print("Document processing complete.")
    # print(f"Text: {document_object.text}")
    print(len(document_object.text))
    data = document_object.text

