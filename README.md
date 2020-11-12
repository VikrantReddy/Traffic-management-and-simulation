# Traffic-management-and-simulation

A project for analysing and normalizing traffic.

# Routing ....
 Progress : Working
 
# Normalizing Traffic ....
 Progress : 
 
## How to set up and use the API :
 
# 1. Install necessary files : 
  ```python
  pip install -r requirements.txt
  ```
# 2. Move to the folder "AskMap" :
 ```
 cd AskMap
 ```
# 3. Perform the following command :
 ```python
 python manage.py runserver
 ```
 This is assuming that you have installed djangorestframework 
 
# 4. To view results do the following Python commands on the command line :
 ```python
 import requests
 
 url  = "http://127.0.0.1:8000/getmaps/"
 data = "1"
 headers = {  
        'Content-Type': 'text/plain'
       }
 res = requests.request("POST", url, headers=headers, data = data)
 print(res.text.encode(''utf8'))
 ```
 This will give the JSON content of the second map.
 For other maps change the "data" number.
 
 ## Other Maps will be done soon . To view JSON of present map : /AskMap/maps.json
 
 
