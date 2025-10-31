# DVM Backend Task 1

## User Manual

To use the command line app, clone the repo and run:
```shell
python main.py -h
```

Example command to view all purchased tickets by user 'foo':
```shell
python main.py --user foo -v
```



## Functionality Implemented

1. Users can see a list of all the metro stations available.
2. Users can purchase a ticket from one metro station to another.
3. Users can see their purchased tickets.
4. Each ticket has a unique ID associated with it. (generated using Python's uuid library)
5. The price of a ticket is based on how many stations the user will cross on the shortest path to their destination.
6. There can be multiple metro lines, and some stations are expected to act as crossroads between 2 or more lines, which allows passengers to change lines.
7. Users can purchase tickets to travel between stations on different lines.
8. You must provide a list of instructions to assist the user in case there is a line change between the origin and the destination.
9. Make multiple CSV files to store data for each different class. You can populate the actual objects in these files at the start of the program or as and when it is required.

## About

To find the shortest path between two stations, an implementation of Dijkstra's algorithm is the most effective, since the weight of all connections/tracks/edges is non-negative. Since the problem relates to a metro network, naturally the nodes are the stations, the connections between the stations make up the edges, and the metro lines simply represent a group of stations.

After computing the shortest path, iterate through each station/node, check if there is a line change (for [8](#functionality)), and compute the ticket cost.

### Pseudocode

```c
when purchase is made:
Dijkstra(stations and their connections [the graph], start, stop) -> shortest_path

for station in shortest_path
    if next_station is on a different line: inform user

update database after calculating the price

when user wants to view stations/tickets bought:
show database entries
```
