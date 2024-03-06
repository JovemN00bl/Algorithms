#breadth-first search - BFS
from collections import deque

graph = {}
graph["you"] = ["Alice", "Bob", "Claire"]
graph["Bob"] = ["Peggy", "Anuj"]
graph["Alice"] = ["Peggy"]
graph["Claire"] = ["thom", "jonny"]
graph["thom"] = []
graph["jonny"] = []
graph["Peggy"] = []
graph["Anuj"] = []

def person_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    verified = []

    while search_queue:
        person = search_queue.popleft()
        if not person in verified:
            if person_seller(person):
                print(person + ' is manga seller!')
                return True
            else:
                search_queue += graph[person]
                verified.append(person)
    return False

search(graph["you"])