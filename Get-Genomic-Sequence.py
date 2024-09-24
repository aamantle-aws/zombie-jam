import boto3
import json
import pandas as pd

client = boto3.client('lambda', region_name='us-east-1')

def invoke_lambda():
    response = client.invoke(
        FunctionName='JAM-Quigley-Get-Data',
        InvocationType='RequestResponse'
    )
    
    # Read the response payload
    response_payload = response['Payload'].read().decode('utf-8')
    
    # Parse the JSON response
    result = json.loads(response_payload)
    
    # Extract the body
    body = json.loads(result['body'])

    # Convert the JSON list to a DataFrame
    df = pd.DataFrame(body)

    # Print the DataFrame
    print(df)

def main():
    invoke_lambda()


if __name__ == "__main__":
    main()
