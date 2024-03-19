from openai import OpenAI

client = OpenAI()


def handle_openai_request(
    messages, model="gpt-3.5-turbo-0125", response_format="json_object"
):
    response = client.chat.completions.create(
        model=model,
        response_format={"type": response_format},  # can be json_object also
        messages=messages,
    )
    return response.choices[0].message.content


# [
#     {"role": "system", "content": system_prompt},
#     {"role": "user", "content": "cucumber, onion, tomato"},
# ] gpt-3.5-turbo-0125
