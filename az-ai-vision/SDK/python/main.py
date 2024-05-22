import os
from dotenv import load_dotenv
from pprint import pprint
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential


def main():
    try:
        load_dotenv()
        ai_api_key = os.environ["API_KEY"]
        ai_api_endpoint = os.environ["ENDPOINT_URI"]
    except KeyError:
        print("Missing environment variable API_KEY or ENDPPOINT_URI")
        print("Ensure environment variables are present before running program")
        exit()
    
    image_url = {
    'url': 'https://aka.ms/azsdk/image-analysis/sample.jpg'
    }


    print(image_url['url'])
    
    client = ImageAnalysisClient(endpoint=ai_api_endpoint, credential=AzureKeyCredential(ai_api_key))
    image_analysis_result = client.analyze_from_url(image_url=image_url['url'], visual_features=[VisualFeatures.OBJECTS])

    if image_analysis_result.items is not None:
        print("Image Analysis: ")
        pprint(image_analysis_result.objects.items)


if __name__ == '__main__':
    main()