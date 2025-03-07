import json

import boto3
from botocore.exceptions import ClientError
from pydantic import BaseModel

# Configuration
model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"
region = "ap-southeast-2"

# Initialize the bedrock client
client = boto3.client("bedrock-runtime", region_name=region)


# Define the structure of the response from the model.
class CalendarEvent(BaseModel):
    event_type: str
    date: str
    time: str
    attendees: list[str]


# Format the request payload body using the model's native structure.
native_request = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 200,
    "temperature": 0,
    "messages": [
        {
            "role": "assistant",  # The message for controlling system behavior.
            "content": [
                {
                    "type": "text",
                    "text": "Extract structured event details and output in JSON format.",
                }
            ],
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Schedule a meeting with John next Tuesday at 3pm?",
                }
            ],
        },
    ],
}

# Convert the native request to JSON.
request = json.dumps(native_request)

try:
    # Invoke the model with the request.
    response = client.invoke_model(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

# Decode the response body.
model_response = json.loads(response["body"].read())
print(model_response)

# Extract and print the response text.
response_text = model_response["content"][0]["text"]
print(CalendarEvent(**json.loads(response_text)))
