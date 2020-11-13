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
 print(res.text.encode("utf8"))
 ```
 This will give the JSON content of the first map.
 For other maps change the "data" number.
 
 ## Other Maps will be done soon . To view JSON of present map : /AskMap/maps.json
 ## 3 Maps added. JSON for the 3rd map:
 ```JSON
 {
        "name": "graph - 3",
        "graph-object": {
            "a": "0 h",
            "b": "0 g",
            "c": "0 1",
            "d": "1 2",
            "e": "f 1",
            "f": "e 2",
            "h": "a 1"
        },
        "lights": [
            "a b c",
            "c e d h",
            "g f d"
        ],
        "cars_on_road": {
            "a": {
                "traffic": 0,
                "length": 8
            },
            "b": {
                "traffic": 0,
                "length": 6
            },
            "c": {
                "traffic": 0,
                "length": 10
            },
            "d": {
                "traffic": 0,
                "length": 5
            },
            "e": {
                "traffic": 0,
                "length": 10
            },
            "f": {
                "traffic": 0,
                "length": 7
            },
            "g": {
                "traffic": 0,
                "length": 7
            },
            "h": {
                "traffic": 0,
                "length": 7
            },
            "light-0": {
                "traffic": 0,
                "length": 6
            },
            "light-1": {
                "traffic": 0,
                "length": 8
            },
            "light-2": {
                "traffic": 0,
                "length": 8
            }
        }
    }
```
 
 
