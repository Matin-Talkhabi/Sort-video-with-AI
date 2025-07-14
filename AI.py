from openai import OpenAI


def OpenAI_API(base_url , api_key , model , content):
    print(content)
    if not model:
        model = "openai/gpt-4o-mini"
    client = OpenAI(
    base_url= base_url,
    api_key= api_key,
    )

    completion = client.chat.completions.create(
    model=model,
    messages=[
        {
        "role": "user",
        "content": content
        }
    ]
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content