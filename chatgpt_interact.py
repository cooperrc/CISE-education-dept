import openai
import datetime
import argparse

filename = datetime.datetime.now()

f = open(filename.strftime("%Y_%m_%d-%H_%M")+".txt", "w")

openai.api_key = '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' #os.getenv("OPENAI_API_KEY")

messages = [
 {"role": "system", "content" : "You're a kind helpful assistant"}
]

parser = argparse.ArgumentParser(description = 'optionally add text from a file')

parser.add_argument("filename", type = str)
args = parser.parse_args()
print(args.filename)
try:
	inputtxt = open(args.filename, 'r')
	messages.append({"role": "user", "content": inputtxt.read()})
except NameError:
	print('no file given')


#content = input("User: ")
#messages.append({"role": "user", "content": content})
#
#completion = openai.ChatCompletion.create(
#  model="gpt-3.5-turbo",
#  messages=messages
#)
#
#chat_response = completion.choices[0].message.content
#print(f'ChatGPT: {chat_response}')
#messages.append({"role": "assistant", "content": chat_response})

while True:
    content = input("User: ")
    if content.lower() == 'end' or content.lower() == 'exit':
        break
    messages.append({"role": "user", "content": content})
    f.write(content)
    f.write('\n\n')

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    f.write(chat_response)
    f.write('\n\n')
    messages.append({"role": "assistant", "content": chat_response})
f.close()
