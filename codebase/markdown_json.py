from google.genai import types
import base64
from client import client
import json
from google import genai
from client import get_json
from prompts import sys_prompt, prompt

def generate(data, client=client):
  final = {}
  msg1_text1 = types.Part.from_text(text=prompt)
  si_text1 = sys_prompt

  model = "gemini-2.5-flash-preview-05-20"
  contents = [
    types.Content(
      role="user",
      parts=[
        msg1_text1
      ]
    ),
  ]

  generate_content_config = types.GenerateContentConfig(
    temperature = 0.1,
    top_p = 1,
    seed = 0,
    max_output_tokens = 65535,
    system_instruction=[types.Part.from_text(text=si_text1)],
    thinking_config=types.ThinkingConfig(
      thinking_budget=1024,
    ),
  )

  response = client.models.generate_content(
    model = model,
    contents = contents,
    config = generate_content_config,
    )
  result = response.text
  # result = get_json(data)
  json_str = result.replace("```json","").replace("```","")
  data = json.loads(json_str)
  return result