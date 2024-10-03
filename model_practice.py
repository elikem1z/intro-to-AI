from openai import OpenAI

#API key
my_key = '' 

#List of keywords to make picture
image_keywords =['draw', 'picture', 'image', 'graphic','photo', 'visual']
# Connecting to OpenAI with API Key
client = OpenAI(api_key=my_key)
# Bool to determine if we're talking to chat GPT
ready_for_command = True

# Function to send command off to Chat CPT and retrieve an answer
def process_command(command):
    global ready_for_command
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": command}
        ]
    )
    text = completion.choices[0].message.content
    print(text)

# Function to generate images
def generate_image(command):
    response = client.images.generate(
        model='dall-e-3',
        prompt=command,
        size='1024x1024',
        quality='standard',
        n=1
    )

    image_url = response.data[0].url
    print(image_url)

while (True):
    command = input('Enter your Chat GPT command\n')
    # Loop to determine if we want pictures or a GPT answer based on wake word list
    if any(word in command for word in image_keywords):
        generate_image(command)
    else:
        process_command(command)
