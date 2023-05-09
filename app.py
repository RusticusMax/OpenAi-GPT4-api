## https://platform.openai.com/examples/default-text-to-command

import os
import openai

openai.api_key = os.getenv("THE_KEY")

print("Sending prompt to OpenAI, with key: " + openai.api_key + "\n")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Describe an elephant to a blind person",
  temperature=0,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.2,
  presence_penalty=0.0,
  stop=["\n"]
)

print ("Response: <", response, ">")