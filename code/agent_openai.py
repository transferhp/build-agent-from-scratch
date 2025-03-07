import json

import httpx
from dotenv import load_dotenv
from openai import OpenAI

# Load the OpenAI API key from the .env file.
load_dotenv()

# Initialize the OpenAI client and disable SSL verfication (not for production).
client = OpenAI(http_client=httpx.Client(verify=False))


# Define a get_weather function to be used as an external tool.
def get_weather(city):
    """Simulates fetching weather data for a given city."""
    sample_weather = {
        "New York": {"temperature": 22, "condition": "Sunny"},
        "London": {"temperature": 15, "condition": "Cloudy"},
        "Tokyo": {"temperature": 18, "condition": "Rainy"},
    }
    return sample_weather.get(city, {"temperature": "Unknown", "condition": "Unknown"})


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a weather assistant."},
        {"role": "user", "content": "What’s the weather like in London?"},
    ],
    functions=[
        {
            "name": "get_weather",
            "description": "Fetches the current weather for a given city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "Name of the city"},
                },
                "required": ["city"],
            },
        }
    ],
    function_call="auto",
)

# Extract the response message and function call from the response.
message = response.choices[0].message
if message.function_call:
    function_name = message.function_call.name
    arguments = json.loads(message.function_call.arguments)

    if function_name == "get_weather":
        result = get_weather(arguments["city"])
        print(
            f"Weather in {arguments['city']}: {result['temperature']}°C, {result['condition']}"
        )
