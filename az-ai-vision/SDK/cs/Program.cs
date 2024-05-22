using System;
using Azure;
using Azure.AI.Vision.ImageAnalysis;
using System.Text;
using System.Text.Json;
using Microsoft.Extensions.Configuration;

namespace AZAIVISION_SDK;

class Program 
{
    // set API Key and AI Services Endpoint
    // set image URL that will be passed to Azure AI Vision for analysis
    static string? AiApiKey = string.Empty;
    static string? AiEndPointURI = string.Empty;
    const string ImageURL = "https://aka.ms/azsdk/image-analysis/sample.jpg";

    static void Main(string[] args)
    {
       // Read data from appsettings.json for api key and ai endpoint uri
        try 
        {
            IConfigurationBuilder builder = new ConfigurationBuilder().AddJsonFile("appsettings.json");
            IConfiguration configuration = builder.Build();
            AiApiKey = configuration["APIKey"];
            AiEndPointURI = configuration["AiEndPoint"];
        }
        catch(Exception ex)
        {
            Console.WriteLine(ex.Message);
        }

        // authenticate with azure ai vision using api key
        ImageAnalysisClient client = new ImageAnalysisClient(
            new Uri(AiEndPointURI!), new AzureKeyCredential(AiApiKey!)
        );

        // use azure ai vision to analyze image based on url
        ImageAnalysisResult result = client.Analyze(new Uri(ImageURL), VisualFeatures.Objects);

        // print results of objects detected to the console
        Console.WriteLine("Image analysis Results: ");
        foreach (DetectedObject detectedObject in result.Objects.Values)
        {
            Console.WriteLine($" Object: {detectedObject.Tags.First().Name}");
        }
    }
}