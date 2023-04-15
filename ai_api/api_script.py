import os
import glob

files = glob.glob('images/*')
for f in files:
    os.remove(f)
    
    
files = glob.glob('processed/*')
for f in files:
    os.remove(f)

from google.api_core.client_options import ClientOptions
from google.cloud import documentai_v1 as documentai
from dotenv import load_dotenv

load_dotenv()

LOCATION = os.environ["LOCATION"]
PROJECT_ID = os.environ["PROJECT_ID"]
PROCESSOR_ID = os.environ["PROCESSOR_ID"]
MIME_TYPE = 'application/pdf'
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
# print(len(document_object.text))
data = document_object.text


import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

tokens = word_tokenize(data)
print(len(tokens))

def break_up_file(tokens, chunk_size, overlap_size):
    if len(tokens) <= chunk_size:
        yield tokens
    else:
        chunk = tokens[:chunk_size]
        yield chunk
        yield from break_up_file(tokens[chunk_size-overlap_size:], chunk_size, overlap_size)

def break_up_file_to_chunks(s, chunk_size=2000, overlap_size=100):
    # with open(filename, 'r') as f:
    #     text = f.read()
    # tokens = word_tokenize(text)
    return list(break_up_file(s, chunk_size, overlap_size))

chunks = break_up_file_to_chunks(tokens)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {len(chunk)} tokens")
    
    

def convert_to_detokenized_text(tokenized_text):
    prompt_text = " ".join(tokenized_text)
    prompt_text = prompt_text.replace(" 's", "'s")
    return prompt_text

import os
import openai

openai.api_key = os.environ["OPENAI_API"]

qa = ''

for i, chunk in enumerate(chunks):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": convert_to_detokenized_text(chunks[i]) + " \n Using only the information provided above and not using the general knowledge of chatgpt, make 10 unique and truthful question and answer pairs using the format:\nQ:\nA:"}
    ]
  )

  # print('\n' + completion.choices[0].message.content)
  qa += completion.choices[0].message.content + '\n'
  

def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string

# with  open('qa.txt' , 'w+') as f:
    # f.write(qa)
    # f.close()

q , a = [] , []

qa_list = qa.split('\n')

for sentence in qa_list:
    if sentence:
        if sentence[0] == 'Q': q.append(remove_suffix(sentence, '\n'))
        if sentence[0] == 'A': a.append(remove_suffix(sentence, '\n'))


qa_pairs = list(zip(q,a))



# import io
# import fitz
# from PIL import Image

# file = FILE_PATH
# # open the file
# pdf_file = fitz.open(file)

# # iterate over pdf pages
# for page_index in range(len(pdf_file)):
    # # get the page itself
    # page = pdf_file[page_index]
    # image_list = page.get_images()
    # # printing number of images found in this page
    # if image_list:
        # print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    # else:
        # print("[!] No images found on page", page_index)
    # for image_index, img in enumerate(page.get_images(), start=1):
        # # get the XREF of the image
        # xref = img[0]
        # # extract the image bytes
        # base_image = pdf_file.extract_image(xref)
        # image_bytes = base_image["image"]
        # # get the image extension
        # image_ext = base_image["ext"]
        # # load it to PIL
        # image = Image.open(io.BytesIO(image_bytes))
        # # save it to local disk
        # image.save(open(f"images/image{page_index+1}_{image_index}.{image_ext}", "wb"))


# import tensorflow as tf
# import os
# import numpy as np
# import cv2

# def preprocess_bytes(byte_string):
    # with open(byte_string, 'rb') as f:
        # img_array = np.asarray(bytearray(f.read()), dtype="uint8")
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # img_resized = cv2.resize(img, dsize=(32, 32), interpolation=cv2.INTER_CUBIC)
        # return img_resized
    
    


# img = tf.data.Dataset.list_files('images/*.png')


# img_arr = []

# img_iterator = img.as_numpy_iterator()

# while True:
    # try:
        # img_arr.append(preprocess_bytes(img_iterator.next()))
    # except:
        # break

# img_arr = np.array(img_arr)



# import keras

# file_path = f"./modelsave/model2.h5"
# model = keras.models.load_model(file_path)
# pred = model.predict(img_arr)

# ans = [[0,0,0]]*len(pred)
# for q in range(len(pred)):
    # for a in range(len(pred[q])):
        # # print(pred[q][a]/1 > 0.8)
        # if pred[q][a]/1 > 0.8: ans[q][a] =1
        # else: ans[q][a] = 0
        

# from os import listdir
# from os.path import isfile, join
# onlyfiles = [f for f in listdir('images/')]
# print(onlyfiles)
# filtered = []
# idx = 0
# for a,b,c in ans:
    # if a  == 1 or b == 1: filtered.append(onlyfiles[idx])
    # idx +=1
    
# print(len(filtered))
# print(filtered)  

# import cv2 
# import easyocr
# from datetime import datetime

# reader = easyocr.Reader(['en'], gpu = True)


# names = []
# for i in onlyfiles:
    # boxes = reader.readtext(f'images/{i}')
    # img = cv2.imread(f"images/{i}")
    # im2 = img.copy()
    # print(i)
    # for box in boxes:
        # x, y, w, h = int(box[0][0][0]), int(box[0][0][1]), int(box[0][1][0] - box[0][0][0]), int(box[0][0][1] - box[0][2][1]) 
        
        # # Draw the bounding box on the text area
        # rect=cv2.rectangle(im2, (x, y), (x + w, y - h), (0, 255, 0), 2)
        
        # # Crop the bounding box area
        # cropped = im2[y:y - h, x:x + w]
        
        # cv2.imwrite(f'processed/rectanglebox-{i}.jpg',rect)
    # if len(boxes) > 0: names.append('processed/rectanglebox-{i}.jpg')
# print(names)


# W
