import random
from threading import Thread
import time
import asyncio

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
  
    async def travel(self):
        visited = set()
        visited.add(self.start)
        self.path.append(str(self.start))
        self.road = self.start

        while self.road != self.end:           
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
                await passvalue
            

            cars_on_road[self.road]-=1
            cars_on_road[nextroad]+=1

            self.road = nextroad
            visited.add(self.road)

            self.path.append(str(self.road))
        
        print(f"Path taken by {self.carid} is {' => '.join(self.path)}")

    def __repr__(self):
        return f"Car Id: {self.carid}, Begin: {self.start}, Dest: {self.end}"
             
    def __str__(self):
        if self.road != self.end:
          return f"The car is at {self.road} travelling at {self.carid} Kmph" 


class TrafficLight:
    def __init__(self,road0=None,road1=None,road2=None,road3=None):
        self.roads = {}
        self.roads.update({road0:False})
        self.roads.update({road1:False})
        self.roads.update({road2:False})
        self.roads.update({road3:False})

    def change_status(self,road):
        self.roads[road] = not self.roads[road]  

    def traffic_logic(self):
        print("The game has begun")
        global stop_lights
        while not stop_lights:
            for road in self.roads:
                if road is None: 
                    continue

                self.change_status(road)
                # print(road + " began")
                time.sleep(3)
                # print(road +  " Stopped")
                self.change_status(road)   
    
    def __repr__(self):
        return "Traffic Light"
    
    def __str__(self):
        return "Traffic Light"

    
    def smart_traffic_logic(self):
        global smart_stop_lights

        print("The game has begun")
        
        while not smart_stop_lights:
            # print(smart_stop_lights)
            mean = apparent_mean()

            for road in self.roads:
                if road is None: 
                    continue

                if cars_on_road[road] < 1:
                    wait_time = 3
                else:
                    smart_time = ((cars_on_road[road] - mean)/cars_on_road[road])
                    wait_time = 8 + smart_time * 3 if 8 + smart_time * 3 < cars_on_road[road] else cars_on_road[road]


                # print(f"{wait_time} seconds")
                
                self.change_status(road)
                # print(road + " began")
                time.sleep(abs(wait_time))
                # print(road +  " Stopped")
                self.change_status(road)            

    async def can_pass(self,road):
        while not self.roads[road]:
            time.sleep(random.randint(0,100)%3)    
        return True

class Road:
    def __init__(self,length,no_of_cars):
        self.length = length
        self.no_of_cars = no_of_cars



def randroad():
    return {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f"}[random.randint(0,5)]



def apparent_mean():
    total_cars = 0
    
    equvivalent_roads = 0

    for no_of_cars in cars_on_road.values():
        total_cars += no_of_cars
        equvivalent_roads = equvivalent_roads + 0 if no_of_cars < 1 else equvivalent_roads + 1 

    return total_cars/equvivalent_roads if equvivalent_roads > 0 else 0



if __name__ == "__main__":

    light = TrafficLight("a","b","e")
    light1 = TrafficLight("d","f")

    cars_on_road = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,light:0,light1:0,}

    stop_lights = False #Kill signal
    smart_stop_lights = False #Kill signal

    traffic_light_thread = Thread(target=light.smart_traffic_logic)
    traffic_light_thread.start()
    traffic_light_thread1 = Thread(target=light1.smart_traffic_logic)
    traffic_light_thread1.start()

# Create the dictionary with graph elements
    graph = { "a" : [light,"e","f"],
            "b" : [light,"c"],
            "c" : ["d","f","b"],
            "d" : ["e","c",light1],
            "e" : ["d",light,"a"],
            "f" :["a","c",light1],
            light : ["a","e","d"],
            light1:["d","f"],
            }
    

    cars = [Car(" ",i,"a","b") for i in range(12)]
    cars += [Car(" ",i,"b","a") for i in range(12,15)]
    cars += [Car(" ",i,"b","d") for i in range(15,26)]
    cars += [Car(" ",i,"d","c") for i in range(17,29)]

    for car in cars:
        print(car.__repr__())

    for car in cars:
        cars_on_road[car.start] += 1


    threads = []
    for i in range(len(cars)):
        x = Thread(target=cars[i].wrapper)
        threads.append(x)
        x.start()
    
    for thread in threads:
        while thread.is_alive():
            continue 

    stop_lights = True #Kill signal
    smart_stop_lights = True #Kill signal
        





        