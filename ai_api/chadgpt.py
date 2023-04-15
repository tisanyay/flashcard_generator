import os
import openai
from dotenv import load_dotenv

load_dotenv()

def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string

def convert_to_detokenized_text(tokenized_text):
    prompt_text = " ".join(tokenized_text)
    prompt_text = prompt_text.replace(" 's", "'s")
    return prompt_text

def generate_qa(chunks):
    qa = ''
    openai.api_key = os.environ['OPENAI_API']

    for i, chunk in enumerate(chunks):
      completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "user", "content": convert_to_detokenized_text(chunks[i]) + " \n Using only the information provided \
                  above and not using the general knowledge of chatgpt, make 10 unique and truthful question and answer \
                  pairs using the format:\nQ:\nA:"}
        ]
      )

      qa += completion.choices[0].message.content + '\n'
      
    q , a = [] , []

    qa_list = qa.split('\n')

    for sentence in qa_list:
        if sentence:
            if sentence[0] == 'Q': q.append(remove_suffix(sentence, '\n'))
            if sentence[0] == 'A': a.append(remove_suffix(sentence, '\n'))


    qa_pairs = list(zip(q,a))
    return qa_pairs
