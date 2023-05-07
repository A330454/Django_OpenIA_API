import openia
from django.conf import settings

def generate_openia_text(prompt):
    openia.api.key = settings.OPEN_API_KEY
    response = openia.Completion.create(
        engine='davinci',
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()