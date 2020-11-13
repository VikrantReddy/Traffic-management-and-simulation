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
        "no_of_roads": 8,
        "road_string": "a b c d e f g h",
        "no_of_lights": 3,
        "light_string": "light-0 light-1 light-2",
        "roads_with_lights": {
            "light-0": "a b c",
            "light-1": "e d c h",
            "light-2": "g f d"
        },
        "name": "graph - 3",
        "graph-object": {
            "a": "light-0 h",
            "b": "light-0 g",
            "c": "light-0 light-1",
            "d": "light-1 light-2",
            "e": "f light-1",
            "f": "e light-2",
            "h": "a light-1",
            "light-0": "a b c",
            "light-1": "c e d h",
            "light-2": "g f d"
        },
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
 
 
