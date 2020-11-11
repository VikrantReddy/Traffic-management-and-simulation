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
  
    # async def travel(self):
    #     visited = set()
    #     visited.add(self.start)
    #     self.path.append(str(self.start))
    #     self.road = self.start

    #     while self.road != self.end:  
    #         self.time_taken += timetopass(self.road)         
    #         cango = [x for x in graph[self.road] if x not in visited]
            
    #         if len(cango) < 1:
    #             lucky_road = graph[self.road][random.randint(0,10)%len(graph[self.road])]
    #             visited.remove(lucky_road)
    #             cango = [lucky_road]          

    #         if self.end not in cango:
    #             # ax = {x:cars_on_road[x]["traffic"] for x in cango}
    #             # ay = max(ax,key=ax.get)

    #             # nextroad = ay
    #             cango = [x for x in graph[self.road] if x not in visited]
    #             nextroad = cango[random.randint(0,10)%(len(cango))]

    #             if nextroad in visited: #or cars_on_road[nextroad]["traffic"]>=15
    #                 continue
    #             elif isinstance(nextroad,TrafficLight):
    #                 passvalue = nextroad.can_pass(self.road) 
    #                 await passvalue

    #         else:
    #             nextroad = self.end



    #         cars_on_road[self.road]["traffic"]-=1
    #         cars_on_road[nextroad]["traffic"]+=1 

    #         self.road = nextroad
    #         visited.add(self.road)

    #         self.path.append(str(self.road))
        
    #     print(f"Path taken by {self.carid} is {' => '.join(self.path)}")


    # def __repr__(self):
    #     return f"Car Id: {self.carid}, Begin: {self.start}, Dest: {self.end}. Time:{self.time_taken}"
             
    # def __str__(self):
    #     if self.road != self.end:
    #       return f"The car is at {self.road} travelling at {self.carid} Kmph" 


class TrafficLight:
    def __init__(self,road0=None,road1=None,road2=None,road3=None):
        self.roads = {}
        self.roads.update({road0:{"light":False,"wait":0}})
        self.roads.update({road1:{"light":False,"wait":0}})
        self.roads.update({road2:{"light":False,"wait":0}})
        self.roads.update({road3:{"light":False,"wait":0}})

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



if __name__ == "__main__":

    light = TrafficLight("b","e","a")
    light1 = TrafficLight("d","f")

    cars_on_road = {"a":{"traffic":0,"length":8},
                    "b":{"traffic":0,"length":6},
                    "c":{"traffic":0,"length":10},
                    "d":{"traffic":0,"length":5},
                    "e":{"traffic":0,"length":10},
                    "f":{"traffic":0,"length":7},
                    light:{"traffic":0,"length":6},
                    light1:{"traffic":0,"length":8},
                    }

    stop_lights = False #Kill signal
    smart_stop_lights = False #Kill signal

    traffic_light_thread = Thread(target=light.traffic_logic)
    traffic_light_thread.start()
    traffic_light_thread1 = Thread(target=light1.traffic_logic)
    traffic_light_thread1.start()

# Create the dictionary with graph elements
    graph = { "a" : [light,"e","f"],
            "b" : [light,"c"],
            "c" : ["d","f","b"],
            "d" : ["e","c",light1],
            "e" : ["d",light,"a"],
            "f" :["a","c",light1],
            light : ["a","e","b"],
            light1:["d","f"],
            }
    
    # for road in cars_on_road:
    #     cars_on_road[road]["length"] = random.randint(4,10)

    cars = [Car(" ",i,"a","b") for i in range(5)]
    cars += [Car(" ",i,"b","a") for i in range(5,8)]
    cars += [Car(" ",i,"b","d") for i in range(8,12)]
    cars += [Car(" ",i,"d","c") for i in range(12,14)]    
    cars += [Car(" ",i,"c","d") for i in range(14,18)]
    cars += [Car(" ",i,"d","a") for i in range(18,23)]

    # for car in cars:
    #     print(car.__repr__())

    for car in cars:
        cars_on_road[car.start]["traffic"] += 1



    threads = []
    for i in range(len(cars)):
        x = Thread(target=cars[i].wrapper)
        time.sleep(1)
        threads.append(x)
        x.start()
    
    for thread in threads:
        while thread.is_alive():
            continue 

    stop_lights = True #Kill signal
    smart_stop_lights = True #Kill signal
        

    ave = 0
    for car in cars:
        ave += car.time_taken

    print(ave/len(cars))

    # print(cars_on_road)





        