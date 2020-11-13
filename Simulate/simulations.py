import random
from threading import Thread
import time
import asyncio
import json

class Car:
    def __init__(self,road,carid,start,end):
        self.road = road
        self.carid = carid
        self.start = start
        self.end = end
        self.path = []
        self.time_taken = 0.0

    def wrapper(self):
        asyncio.run(self.travel())
    
    def smart_wrapper(self):
        asyncio.run(self.smart_travel())

    async def travel(self):
        visited = set()
        visited.add(self.start)
        self.path.append(str(self.start))
        self.road = self.start

        while self.road != self.end:
            if not isinstance(self.road,TrafficLight):    
                self.time_taken += timetopass(self.road)

            cango = [x for x in graph[self.road] if x not in visited]
            
            if len(cango) < 1:
                lucky_road = graph[self.road][random.randint(0,10)%len(graph[self.road])]
                visited.remove(lucky_road)
                cango = [lucky_road]          

            nextroad = cango[random.randint(0,10)%(len(cango))]

            if nextroad in visited: #or cars_on_road[nextroad]>=15
                continue
            elif isinstance(nextroad,TrafficLight):
                passvalue = nextroad.can_pass(self.road) 
                self.time_taken += nextroad.roads[self.road]["wait"]
                await passvalue
            

            cars_on_road[self.road]["traffic"]-=1
            cars_on_road[nextroad]["traffic"]+=1

            self.road = nextroad
            visited.add(self.road)

            self.path.append(str(self.road))
        
        print(f"Path taken by {self.carid} is {' => '.join(self.path)}")
  
    async def smart_travel(self):
        visited = set()
        visited.add(self.start)
        self.path.append(str(self.start))
        self.road = self.start

        while self.road != self.end:  
            if not isinstance(self.road,TrafficLight):
                self.time_taken += timetopass(self.road)         
            
            cango = [x for x in graph[self.road] if x not in visited]
            
            if len(cango) < 1:
                lucky_road = graph[self.road][random.randint(0,10)%len(graph[self.road])]
                visited.remove(lucky_road)
                cango = [lucky_road]          

            if self.end not in cango:
                cango = [x for x in graph[self.road] if x not in visited]
                nextroad = cango[random.randint(0,10)%(len(cango))]

                if nextroad in visited: #or cars_on_road[nextroad]["traffic"]>=15
                    continue
                elif isinstance(nextroad,TrafficLight):
                    passvalue = nextroad.can_pass(self.road) 
                    await passvalue

            else:
                nextroad = self.end



            cars_on_road[self.road]["traffic"]-=1
            cars_on_road[nextroad]["traffic"]+=1 

            self.road = nextroad
            visited.add(self.road)

            self.path.append(str(self.road))
        
        print(f"Path taken by {self.carid} is {' => '.join(self.path)}")


    # def __repr__(self):
    #     return f"Car Id: {self.carid}, Begin: {self.start}, Dest: {self.end}. Time:{self.time_taken}"
             
    # def __str__(self):
    #     if self.road != self.end:
    #       return f"The car is at {self.road} travelling at {self.carid} Kmph" 


class TrafficLight:
    def __init__(self,args):
        self.roads = {}
        for arg in args:
            self.roads.update({arg:{"light":False,"wait":0}}) 

    def change_status(self,road):
        self.roads[road]["light"] = not self.roads[road]["light"]  

    def traffic_logic(self):
        global stop_lights
        while not stop_lights:
            for road in self.roads:
                if road is None: 
                    continue

                self.roads[road]["wait"]=3
                self.change_status(road)
                # print(road + " began")
                # time.sleep(3)
                # print(road +  " Stopped")
                self.change_status(road)   
    
    def __repr__(self):
        return "Traffic Light"
    
    def __str__(self):
        return "Traffic Light"

    
    def smart_traffic_logic(self):
        global smart_stop_lights

        # print("The game has begun")
        
        while not smart_stop_lights:
            # print(smart_stop_lights)
            mean = apparent_mean([x for x in self.roads if x is not None])

            for road in self.roads:
                if road is None: 
                    continue

                if cars_on_road[road]["traffic"] < 1:
                    wait_time = 1
                else:
                    smart_time = ((cars_on_road[road]["traffic"] - mean)/max(cars_on_road[road]["traffic"],mean))
                    wait_time = 1.5 + smart_time
                
                self.roads[road]["wait"]=wait_time
                # print(wait_time)
                self.change_status(road)
                time.sleep(abs(wait_time))
                self.change_status(road)            

    async def can_pass(self,road):
        while not self.roads[road]["light"]:
            time.sleep(random.randint(0,10)%2)    
        return True


def timetopass(x):
    return cars_on_road[x]["length"] * (cars_on_road[x]["traffic"]/cars_on_road[x]["length"])**(1/2)


def randroad():
    return {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f"}[random.randint(0,5)]



def apparent_mean(args):
    total_cars = 0
    
    equvivalent_roads = 0

    for x in args :
        total_cars += cars_on_road[x]["traffic"]
        equvivalent_roads = equvivalent_roads + 0 if cars_on_road[x]["traffic"] < 1 else equvivalent_roads + 1 

    return total_cars/equvivalent_roads if equvivalent_roads > 0 else 0


def get_data():
    import requests

    url  = "http://127.0.0.1:8000/getmaps/"
    data = "1"
    headers = {  
           'Content-Type': 'text/plain'
      }
    res = requests.request("POST", url, headers=headers, data = data)
    
    return res.text

def get_clean_data():
    data = json.loads(get_data())
    
    lights = data["lights"]
    graph = data["graph"]
    cars_on_road = data["cars_on_road"]

    return lights,graph,cars_on_road


if __name__ == "__main__":

    stop_lights = False #Kill signal
    smart_stop_lights = False #Kill signal

    lights,graph,cars_on_road = get_clean_data()


    for key,value in graph.items():
        graph.update({key:value.strip().split()})

    lightlist = []
    lightthreads = []

    for light in lights:
        roads_connected = light.strip().split()
        lightobj = TrafficLight(roads_connected)
        lightlist.append(lightobj)
        for i in roads_connected:
            graph[i].append(lightobj)
        
        cars_on_road.update({lightobj:{"traffic":0,"length":5}})

        lightthreads.append(Thread(target=lightobj.traffic_logic))

        graph.update({lightobj:roads_connected})


    cars = [Car(" ",i,"a","b") for i in range(5)]
    cars += [Car(" ",i,"b","a") for i in range(5,8)]
    cars += [Car(" ",i,"b","d") for i in range(8,12)]
    cars += [Car(" ",i,"d","c") for i in range(12,14)]    
    cars += [Car(" ",i,"c","d") for i in range(14,18)]
    cars += [Car(" ",i,"d","a") for i in range(18,23)]

    for car in cars:
        cars_on_road[car.start]["traffic"] += 1


    threads = []
    for i in range(len(cars)):
        x = Thread(target=cars[i].wrapper)
        time.sleep(1)
        threads.append(x)
        x.start()

    for lightthread in lightthreads:
        lightthread.start()
    
    for thread in threads:
        while thread.is_alive():
            continue 

    stop_lights = True #Kill signal
    smart_stop_lights = True #Kill signal

    ave = 0
    for car in cars:
        ave += car.time_taken

    print(ave/len(cars))


     #TO-DO
     # generate csv 