# Azure AI Custom Vision

Azure provide two Azure AI Custom Vision for image classification and detection:

1. [Custom Vision Service](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/overview): which is dubbed as legacy in favour of the newer model.
2. [Image Analysis 4.0 service](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/concept-model-customization): which is the new model based on Florence foundational model.

Table comparison between the two models:
> source of the table is Microsoft Learn Documentation

|Area|Custom Vision Service|ImageAnalysis 4.0 Service|
|----|----|----|
|Tasks|Image Classification, Object Detection|Image classification, Object Detection|
|Based Model|CNN|Transformer model|
|Labeling|[customvision.ai](https://www.customvision.ai/)|AML Studio|
|Web Portal|[customvision.ai](https://www.customvision.ai/)|[Vision Studio](https://portal.vision.cognitive.azure.com/gallery/featured)|
|Libraries|REST, SDK|REST, Python sample|
|Min Training data needed| 15 images per category| 2-5 images per category|
|Training Data Stroage|uploaded to service|customer's blob storage account|
|Model Hosting| Cloud & Edge|Cloud Hosting only for now|

## Custom Vision Services

Azure Customer Vision Workflow:
- Create a project in customvision.ai
- Load all the images and data available to the project.
- Label the images with the custom tags
- Train the model for the period of time we prefer.
- Test the model with some Test images.

### Custom Vision, Build an image classification

1. Have an Azure subscription and create Azure Custom Vision services [F0: free tier, S0: $2.00 USD/1000 Transactions]
2. Have a sample images to be uploaded to [customvision.ai](customvision.ai) project. [Sample Image from Microsoft Documentation](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/CustomVision/ImageClassification/Images)
3. Create a project specifying:
    - Name
    - Description 
    - Resource
    - Project Types [Classification, Detection]
    - Classification Types [Multilabel, Multiclass] 
    - Domains
4. Upload the images to the project
5. Create tags and label the images.
6. Train the model then evaluate the classifier. 
7. Test model with uploading a new image, retrain and improve classification.
8. Publish Model to Azure AI Prediction Services or Azure AI Services

> note: Detection will find areas within the image for tagging, classificatio tags the whole image.

> source  [Build Image Classifier Doc](https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/getting-started-build-a-classifier)

Python SDK requires the below packages that can be installed using the `requirements.txt` file

```bash
pip install azure-cognitiveservices-vision-customvision
pip install python-dotenv
```
> note: to get prediction ID resources from Azure Portal, go to Azure AI Custim Image Prediction resources > Resource Management > Properties

## Image Analysis 4.0 Service

// TODO