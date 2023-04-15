import streamlit as st
import requests
import asyncio
from streamlit_lottie import st_lottie
from ai_api.doc_ocr import extract_text
from ai_api.tokenize_text import chunkify
from ai_api.chadgpt import generate_qa
from streamlit_card import card

def generate_flashcards(bytes_data):
    document_object = extract_text(bytes_data)
    chunks = chunkify(document_object.text)
    qa_pairs = generate_qa(chunks)
    return qa_pairs

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- animation asset ---
flashcard_animation = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_jxgqawba.json")
spinning_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_b88nh30c.json")

# --- headers ---
st.set_page_config(page_title="Flashcard Generator", page_icon=":card_index:", layout="wide")

st.subheader("AI card generator")

with st.container():
    left_column, right_column = st.columns((2,1))

    with left_column:
        st.title("Automate flashcard creation by uploading any PDF file")
        st.write("Flashcards are excellent as they exercise active recall when used effectively. However, creating the \
                flashcards are a hassle and is one of the main reasons people don't use them more often. This app \
                aims to solve this issue and make flashcards a viable option for every learner!")
    with right_column:
        st_lottie(flashcard_animation, height=300, key="flashcards")


st.write('---')
uploaded_file = st.file_uploader("Choose a PDF file")


# cols = st.columns(4)

# --- test cards ---
# with cols[1]:
    # card(
      # title="Hello World!",
      # text="Some description",
      # image="http://placekitten.com/200/300",
      # url="https://github.com/gamcoh/st-card"
    # )

# with cols[2]:
    # card(title='answer', text='')


if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # loading_animation = st_lottie(spinning_animation, height=100, key="Please wait...")
    with st.spinner('Generating cards...'):
        qa_pairs = generate_flashcards(bytes_data)

    cols = st.columns(4)

    for q, a in qa_pairs:
        with cols[1]:
            card(title='', text=q)
        with cols[2]:
            card(title='', text=a)

