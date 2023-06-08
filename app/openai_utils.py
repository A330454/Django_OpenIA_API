import openai

openai.api_key = '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'

def gpt3_request(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response['choices'][0]['message']['content']