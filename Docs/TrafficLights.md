
# Traffic Lights control draft

##### [Goal]() : Optimize the traffic signals such that the average time taken at the signal must tend to minimum.

#

```The inefficiency is determined by ```
  - Obsolete time
    - The time given to a particular road even after the road has been cleared
  - Round robin time
    - The time spent on waiting for the road's turn to recur.

> The light may shift when there are no vehicles are on a side and</br>
> The time given to a side must be decided dynamically.

#### Manipulation of the signals can only be done as long as it's ensured that all the roads get their turn and the average weighting period decreases. 

Equations
---
~~~
Variance of the traffic across the mean -> minimum 
The time given to a road shall be t + x[i] where t < T/4
//t is the minimum time given for a road, x is the array of varaible durationations and T is the total time for a round.
~~~


#### Scope for improvment
- The total time for a round doesn't have to be dynamic
  - When the data is analysed for longer durations(months) the total time for a round can also be manipulated.
  - The lights on one side of a road can go to sleep when there is inactivity.
- Emergency situations can be taken into account by detecting unusual amounts for traffic. 
- Piped data from routing to predict upcomming traffic.
- A cost function that learns from it's mistakes and adjusts x[i].

#### Current implmentation plan
 - Will be using dummy data to simulate.
 - Will be used proposed equation for normalizing Traffic by manipulating traffic lights.

