import requests
import os
from dotenv import load_dotenv



def main():
    try:
        load_dotenv()
        # read endpoint and api key from the .env
        # alternatively endpoint and api key can be in host environment variable
        ai_endpoint = os.getenv('ENDPOINT_URI').rstrip('/')
        ai_key = os.getenv('API_KEY')
    except:
        print("Missing environment variables API_KEY and/or ENDPOINT URI")
        print("Ensure environment variables are present before running program")
        exit()
     
    # url for the image to be analyze
    url_data = {
    'url': 'https://github.com/joebq/ai102-repo/raw/main/assets/nature/tree.png'
    }

    # HTTP header
    headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': ai_key
    }

    # paramters for Azure AI Vision API
    param = {
    'features': 'objects',
    'language': 'en',
    }

    # send to Azure Cognitive Services, API Vision Version 3.2
    response = requests.post(f"{ai_endpoint}/vision/v3.2/analyze?objects", headers=headers, json=url_data)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f'Error: {response.json()} ')


if __name__ == '__main__':
    main()

    