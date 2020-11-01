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

    def wrapper(self):
        asyncio.run(self.travel())
  
    async def travel(self):
        visited = set()
        self.road = self.start

        while self.road != self.end:

            nextroad = graph[self.road][random.randint(0,10)%len(graph[self.road])]
            
            if isinstance(nextroad,TrafficLight):
                passvalue = nextroad.can_pass(self.road)

                await passvalue    
            
            elif nextroad in visited or cars_on_road[nextroad]>=5:
                continue
            

            cars_on_road[self.road]-=1
            cars_on_road[nextroad]+=1

            self.road = nextroad
            visited.add(self.road)

    def __repr__(self):
        return f"Car Id: {self.carid}, Begin: {self.start}, Pos: {self.road}, Dest: {self.end}"
             
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
        while True:
            for road in self.roads:
                if road is None: 
                    continue

                self.change_status(road)
                time.sleep(30)
                self.change_status(road)   

    async def can_pass(self,road):
        while not self.roads[road]:
            time.sleep(random.randint(0,100)%5)    
        return True



def randroad():
    return {0:"a",1:"b",2:"c",3:"d",4:"e"}[random.randint(0,4)]



def mean():
    total_cars = 0
    for no_of_cars in cars_on_road.values():
        sum += no_of_cars
    
    return total_cars/len(cars_on_road.values())



if __name__ == "__main__":

    light = TrafficLight("a","b")
    Thread(target=light.traffic_logic).start()

# Create the dictionary with graph elements
    graph = { "a" : [light],
            "b" : [light, "d","c"],
            "c" : ["a", "d","e"],
            "d" : ["e","a","b","c"],
            "e" : ["d","c"],
            light : ["a","b"]
            }

    cars_on_road = {"a":0,"b":0,"c":0,"d":0,"e":0,light:0}

    cars = [Car(" ",i,"a","b") for i in range(2)]
    cars += [Car(" ",i,"b","a") for i in range(2)]

    print(cars)

    for car in cars:
        cars_on_road[car.start] += 1


    threads = []
    for i in range(4):
        x = Thread(target=cars[i].wrapper)
        threads.append(x)
        x.start()
    for thread in threads:
        while thread.is_alive():
            continue 
    print(cars)





        