# Flashcard Generator
### 1. Change to root directory of project
```sh
$ cd $root_directory
```

### 2. Setup virtual environment and activate environment
Create virtual environment
```sh
$ python3 -m venv env
```

Activate the environment
```sh
$ env/bin/activate
```

### 3. Install dependencies
```sh
$ pip install -r requirements.txt
```

### 4. Create .env file
This will add environment variables that will be used the app
> #### **`.env`**
> ```
> PROJECT_ID={PROJECT_ID}
> LOCATION={LOCATION}
> PROCESSOR_ID={PROCESSOR_ID}
> OPENAI_API={OPENAI_API}
> ```
Replace the values in the curly brackets
|key|value|
|---|---|
|PROJECT_ID|The ID generated when you create a project in google cloud|
|LOCATION|The location of the google document AI processor|
|PROCESSOR_ID|The ID of the google document AI processor|
|OPENAI_API|The API key used to generate the flashcards. You can create your own API keys through [openai](https://platform.openai.com/account/api-keys)|

### 5. Create gcloud service account credential json token
You can learn how to create and use your token to access the google document AI API through [here](https://cloud.google.com/iam/docs/keys-create-delete)

### 6. Run streamlit app
```sh
$ streamlit run app.py
```
