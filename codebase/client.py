import tempfile
import os
import vertexai
import base64
from dotenv import load_dotenv
from google import genai
from openai import AzureOpenAI
from prompts import sys_prompt, prompt


load_dotenv()



CREDENTIALS_INFO= base64.b64decode(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
PROJECT= "firstsource-vertex"
GOOGLE_LOCATION= "us-central1"



with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_cred_file:
    temp_cred_file.write(CREDENTIALS_INFO.decode())
    temp_cred_file_path = temp_cred_file.name


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = temp_cred_file_path

vertexai.init(project=PROJECT)

client = genai.Client(
      vertexai=True,
      project=PROJECT,
      location="global",
  )


openai_client = AzureOpenAI(
    azure_endpoint = "https://firstsource.openai.azure.com", 
    api_key = "ee65aca022a74803b2e2d1ff4c373b05",  
    api_version = "2024-02-15-preview"
)


def get_messages(data):
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": prompt}
    ]
    return messages



def get_json(data):
    messages = get_messages(data)
    response = openai_client.chat.completions.create(
        model="gpt-4o-v05-13", 
        messages=messages,
        max_tokens=None,
        temperature=0.1
        )
    return response.choices[0].message.content