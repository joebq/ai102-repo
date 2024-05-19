# Azure AI Vision Services


[Azure AI Vision API Documentation](https://eastus.dev.cognitive.microsoft.com/docs/services/unified-vision-apis-public-preview-2023-04-01-preview/operations/61d65934cd35050c20f73ab6)


```bash
curl -v -X POST "https://*.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2023-04-01-preview?features={array}&model-name={string}&language=en&smartcrops-aspect-ratios={string}&gender-neutral-caption=False"
-H "Content-Type: application/json"
-H "Ocp-Apim-Subscription-Key: {subscription key}"

--data-ascii "{body}" 
```
## Python coode for Azure AI Vision/REST API

```python
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'features': '{array}',
    'model-version': 'latest',
    'language': 'en',
    'smartcrops-aspect-ratios': '{array}',
    'gender-neutral-caption': 'False',
})

try:
    conn = http.client.HTTPSConnection('*.cognitiveservices.azure.com')
    conn.request("POST", "/computervision/imageanalysis:analyze?api-version=2024-02-01&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
```