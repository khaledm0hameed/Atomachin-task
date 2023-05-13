import requests

def googleimgdownload(url,savelocation):
  
    response = requests.get(url)
    if response.status_code == 200:
        with open(savelocation, 'wb') as file:
            file.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download the image.")





 

 

