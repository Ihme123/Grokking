from collections import deque
# Build a graph
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'johnny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['johnny'] = []

mango_sellers = ['anuj', 'clearence']
def person_is_mango_seller(name):
    return name in mango_sellers
    
def breadth_first_search(search_graph, name):
    que = deque()
    # Put the first name into the que
    que.append(name)
    searched_people = []
    while que:
        subject = que.popleft()
        if not subject in searched_people:
            if person_is_mango_seller(subject):
                print('Found! Mango seller is')
                return subject
            # If person is not , add all of his friends to the que
            que += search_graph.get(subject)
            searched_people.append(subject)
    return False

breadth_first_search(graph, 'you')