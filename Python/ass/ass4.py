import openai

openai.api_key = "YOUR_API_KEY"

prompt = "Hello, how can I help you today?"
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)
message = response.choices[0].text.strip()
print(message)