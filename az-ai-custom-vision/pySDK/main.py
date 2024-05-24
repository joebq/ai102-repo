import os, time, uuid 
from dotenv import load_dotenv
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials 


def main():
    load_dotenv()
    try:
        vision_training_endpoint = os.environ["VISION_TRAINING_ENDPOINT"]
        vision_training_key = os.environ["VISION_TRAINING_KEY"]
        vision_prediction_endpoint = os.environ["VISION_PREDCTION_ENDPOINT"]
        vision_prediction_key = os.environ["VISION_PREDICTION_KEY"]
        vision_prediction_resource_id = os.environ["VISION_PREDICTION_RESOURCE_ID"]
    except KeyError as e:
        print(f"Invalid key error {e}")

    # authenticate with Azure AI Custom Image services
    vision_credentials = ApiKeyCredentials(in_headers={"Training-key": vision_training_key})
    trainer = CustomVisionTrainingClient(vision_training_endpoint, vision_credentials)
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": vision_prediction_key})
    predictor = CustomVisionPredictionClient(vision_prediction_endpoint, prediction_credentials)

    # create new Azure AI custom Image project
    iteration_name = "modelClassification"
    print("Creating new Azure AI Custom Image Classification Project ...")
    # create a unique project ID
    project_name = uuid.uuid4()
    project = trainer.create_project(project_name)

    # Add tags
    # tag names reflect the specific tags and classificaiton of this project
    # this project classifies two tags: hemlock and japanese cherry
    hemlock_tag = trainer.create_tag(project.id, "Hemlock")
    cherry_tag = trainer.create_tag(project.id, "Japanese Cherry")

    # upload images
    image_directory = os.path.join(os.path.dirname(__file__), "Images")
    print("Adding Images to project ...")
    image_list = []

    for image_num in range(1, 11):
        file_name = "hemlock_{}.jpg".format(image_num)
        with open(os.path.join (image_directory, "Hemlock", file_name), "rb") as image_contents:
            image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[hemlock_tag.id]))

    for image_num in range(1, 11):
        file_name = "japanese_cherry_{}.jpg".format(image_num)
        with open(os.path.join (image_directory, "Japanese_Cherry", file_name), "rb") as image_contents:
            image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[cherry_tag.id]))

    upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))
    if not upload_result.is_batch_successful:
        print("Image batch upload failed.")
        for image in upload_result.images:
            print("Image status: ", image.status)
        exit(-1)

    # Traing the Project
    print ("Training...")
    iteration = trainer.train_project(project.id)
    while (iteration.status != "Completed"):
        iteration = trainer.get_iteration(project.id, iteration.id)
        print ("Training status: " + iteration.status)
        print ("Waiting 10 seconds...")
        time.sleep(10)
    
    # publish the project after training iteration
    # The iteration is now trained. Publish it to the project endpoint
    trainer.publish_iteration(project.id, iteration.id, iteration_name, vision_prediction_resource_id)
    print ("Done!")

    # Test Prediction Endpoing
    with open(os.path.join (image_directory, "Test/test_image.jpg"), "rb") as image_contents:
        results = predictor.classify_image(
            project.id, iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))



if __name__ == '__main__':
    main()