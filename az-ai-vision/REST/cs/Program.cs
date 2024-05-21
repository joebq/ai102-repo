using System;
using System.Text;
using System.Text.Json;
using Microsoft.Extensions.Configuration;

namespace AZAIVISION;

class Program
{
    // set URL for the image that needs to be analyzed
    const string imageURL        = "https://github.com/joebq/ai102-repo/raw/main/assets/nature/tree.png";

    // Set API Key and AI EndPoint as empty strings
    private static string? apiKey = string.Empty;
    private static string? aiEndPoint = string.Empty;
 

    static async Task Main(string[] args)
    {
        try 
        {
            // read appsettings.json file for API Key and Endpoint
            IConfigurationBuilder builder = new ConfigurationBuilder().AddJsonFile("appsettings.json");
            IConfiguration configuration = builder.Build();
            apiKey = configuration["APIKey"];
            aiEndPoint = configuration["AiEndPoint"];
            Console.WriteLine("Sending Request to Azure AI Services to Analyze Image");
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
        
        // call function that will analze the data
        await AnalyzeImage();
    }

    // class to set the HTTP Body that will be sent with the Post request
    internal class HTTPPayload 
    {
        public required string url { get; set; }
    }


    private static async Task AnalyzeImage()
    {
        try 
        {
            // create new HTTP Client, set the base URI to the API Endpoint and add the API Key to the header 
            var client = new HttpClient();
            client.BaseAddress = new Uri(aiEndPoint!);
            client.DefaultRequestHeaders.Add("Ocp-Apim-Subscription-Key", apiKey);

            var HttpPayload = new HTTPPayload
            {
                url = imageURL
            };
            
            // serialize image class and send content as JSON String
            var ImageJson = JsonSerializer.Serialize(HttpPayload);
            Console.WriteLine(ImageJson);
            var JsonContent = new StringContent(ImageJson, Encoding.UTF8, "application/json");

            // Send to Azure Cognitive Services, API Vision Version 3.2
            var response = await client.PostAsync($"{aiEndPoint}vision/v3.2/analyze?objects", JsonContent);
            if(response.IsSuccessStatusCode)
            {
                // Console.WriteLine(response.ToString());
                var responseContent = response.Content.ReadAsStringAsync().Result;
                Console.WriteLine(responseContent);
            }
            else
            {
                Console.WriteLine($"HTTP Error: {response.StatusCode}");
            }

        }
        catch(Exception ex)
        {
            Console.WriteLine(ex.Message);
        }

    }

}

