try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

dictCitiesH = {
    "Arad"          : 366,
    "Bucharest"     : 0,
    "Craiova"       : 160,
    "Drobeta"       : 242,
    "Eforie"        : 161,
    "Fagaras"       : 178,
    "Giurgiu"       : 77,
    "Hirsova"       : 151,
    "Iasi"          : 226,
    "Lugoj"         : 244,
    "Mehadia"       : 241,
    "Neamt"         : 234,
    "Oradea"        : 380,
    "Pitesti"       : 98,
    "Rimnicu Vilcea": 193,
    "Sibiu"         : 253,
    "Timisoara"     : 329,
    "Urziceni"      : 80,
    "Vaslui"        : 199,
    "Zerind"        : 374,
}

dictCities = {
    "Arad"          : {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Bucharest"     : {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85  },
    "Craiova"       : {"Pitesti": 138, "Drobeta": 120, "Rimnicu Vilcea": 146  },
    "Drobeta"       : {"Mehadia": 75 , "Craiova": 120  },
    "Eforie"        : {"Hirsova": 86 },
    "Fagaras"       : {"Sibiu": 99, "Bucharest": 211 },
    "Giurgiu"       : {"Bucharest": 90 },
    "Hirsova"       : {"Eforie": 86, "Urziceni": 98 },
    "Iasi"          : {"Neamt": 87, "Vaslui": 92 },
    "Lugoj"         : {"Timisoara": 111, "Mehadia": 70 },
    "Mehadia"       : {"Lugoj": 70, "Drobeta": 75 },
    "Neamt"         : {"Iasi": 87 },
    "Oradea"        : {"Zerind": 71, "Sibiu": 151 },
    "Pitesti"       : {"Craiova": 138, "Bucharest": 101, "Rimnicu Vilcea": 97 },
    "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146 },
    "Sibiu"         : {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80 },
    "Timisoara"     : {"Arad": 118, "Lugoj": 111 },
    "Urziceni"      : {"Bucharest": 85, "Hirsova": 98, "Vaslui":  142 },
    "Vaslui"        : {"Urziceni": 142, "Iasi": 92 },
    "Zerind"        : {"Oradea": 71, "Arad": 75 }
}

def sortFunc(item):
    return item["priority"]

def algorithmA():
    start = "Arad"
    goal = "Bucharest"
    frontier = [{"name": start, "priority": 0}]
    
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    
    while len(frontier)>0:
        frontier.sort(key=sortFunc)
        current = frontier.pop(0)['name']
    
        if current == goal:
          break
      
        for next in dictCities[current]:
            new_cost = cost_so_far[current] + dictCities[current][next] 
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + dictCitiesH[next]
                frontier.append({"name" : next, "priority": priority})
                came_from[next] = current
    path = [goal]
    next = came_from[goal]
    while next is not None:
        path.append(next)
        next= came_from[next]
    path.reverse()
    
    print "La ruta es: "
    print (' -> '.join(path))
    print "Con " + str(cost_so_far[goal]) + "km"
    

if __name__ == '__main__':
    algorithmA()