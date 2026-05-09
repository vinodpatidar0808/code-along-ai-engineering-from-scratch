from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

# this is a streaming response, so we can iterate over the response to get the message as it comes in
# for message in client.messages.create(
#     max_tokens=1024,
#     messages=[{
#         "content": "Hello, world",
#         "role": "user",
#     }],
#     model="claude-opus-4-6",
# ):
#   print(message)

# from roadmap 

response = client.messages.create(
  model = "claude-sonnet-4-20250514",
  max_tokens = 256,
  messages = [
    {
      "role": "user",
      "content": "What is a neural network in one sentence?"
    }
  ]
)

print(f"response: {response}")
# print(f"Content: {response.choices[0].message.content}")
print(f" message: {response.content[0].text}")