import requests

response = requests.post(
    'https://sdk.photoroom.com/v1/segment',
    headers = {'x-api-key': '85ec9dcfc4dad1e802961a5266ea0e18d43a670f'},
    files =  
    {
        'image_file': open('test.jpg', 'rb'),
        # 'size': '',
        'format': 'jpg'
    },
)

response.raise_for_status()
with open('photoroom-sdk-result.jpg', 'wb') as f:
	f.write(response.content)