
# Routing draft

##### [Goal]() : Reduce the estimated time of approach(ETA) while traversing from one point to another.

#

```The time taken is determined by```
  - Wait time 
    -  Amount of uncleared traffic ahead of the vehicle  
  - Travel time
    - Distance to the destination 
    - Speed of the vehicle on the road

> Wait time can be decreased by spreading the traffic among all the routes and</br>
> Speed of a vehicle is affected when roads aren't clear.

#### Changing to a longer road is beneficial only when the increase in travel time caused by the increase in distance can be compensated by the decrease in the forthcomming wait time. 

Equations
---
~~~
Change in distance x [Change in average speed +/- k] > 0 
// k is a constant to account for change in vehicles
Change in Wait time + Change in travel time > 0
~~~

#### Planed Implemetation for now 
 - Convert the given map into a graph (Or construct a dummy graph) or take data from an API.
 - Use simple algorithms to find the shorted route based on the weights as 
   - The traffic density
   - Traffic speed for that instant of time in a specific length of route.
   - Length of the route.

#### Scope for improvment
- Take vehicles that aren't a part of the A-B journey into account.
    - Vehicles from outside that have their destination as B.
    - Vehicles on the same road that don't have to reach,
- Once the traffic lights are in control, wait time can be predicted and manipulated better.
- A feedback loop to adjust k (constant) to route more precisely. 
