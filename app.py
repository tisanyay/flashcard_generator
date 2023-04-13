import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- animation asset ---
flashcard_animation = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_jxgqawba.json")

# --- headers ---
st.set_page_config(page_title="Flashcard Generator:double_exclamation_mark:", page_icon=":card_index:", layout="wide")

st.subheader("AI card generator :collision:")

with st.container():
    left_column, right_column = st.columns((2,1))

    with left_column:
        st.title("Automate flashcard creation by uploading any PDF file")
        st.write("Flashcards are excellent as they exercise active recall when used effectively. However, creating the \
                flashcards are a hassle and is one of the main reasons people don't use them more often. This app \
                aims to solve this issue and make flashcards a viable option for every student!")
    with right_column:
        st_lottie(flashcard_animation, height=300, key="flashcards")


st.write('---')
uploaded_file = st.file_uploader("Choose a PDF file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
