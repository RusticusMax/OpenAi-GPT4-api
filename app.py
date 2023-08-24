## https://platform.openai.com/examples/default-text-to-command

import os
import openai
from langchain.llms import OpenAI
from langchain import PromptTemplate
response = "No call made to LLM (MLW)"

question = "wtf"
template = "Question: {question}\nAnswer:"
prompt = PromptTemplate(template=template, input_variables=["question"])

openai.api_key = os.getenv("THE_KEY")
os.environ["OPENAI_API_KEY"] = openai.api_key

llm = OpenAI(temperature=0.9, model="text-davinci-003")


print("Sending prompt to OpenAI, with key: " + openai.api_key + "\n")
# response = openai.Completion.create(
#   model="text-davinci-003",
#   # write a simple prompt for text-davinci-003
#   prompt="which side hustle is likely to be successful?\"\"\"",
#   # prompt="\"\"\"\nUtil exposes the following:\nutil.openai() -> authenticates & returns the openai module, which has the following functions:\nopenai.Completion.create(\n    prompt=\"<my prompt>\", # The prompt to start completing from\n    max_tokens=123, # The max number of tokens to generate\n    temperature=1.0 # A measure of randomness\n    echo=True, # Whether to return the prompt in addition to the generated completion\n)\n\"\"\"\nimport util\n\"\"\"\nCreate an OpenAI completion starting from the prompt \"Once upon an AI\", no more than 5 tokens. Does not include the prompt.\n\"\"\"\n",
#   temperature=0,
#   max_tokens=64,
#   top_p=1.0,
#   frequency_penalty=0.0,
#   presence_penalty=0.0,
#   stop=["\"\"\""]
#)

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Describe an elephant to a blind person",
#   temperature=0,
#   max_tokens=100,
#   top_p=1.0,
#   frequency_penalty=0.2,
#   presence_penalty=0.0,
#   stop=["\n"]
# )

print ("Response: <", response, ">")
