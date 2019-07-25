graph = {}
graph['start'] = {}
graph['start']['a'] = 8
graph['start']['b'] = 4
graph['start']['c'] = 7
graph['a'] = {}
graph['a']['d'] = 10
graph['b'] = {}
graph['b']['d'] = 5
graph['b']['c'] = 1
graph['c'] = {}
graph['c']['fin'] = 8
graph['d'] = {}
graph['d']['fin'] = 5
graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 8
costs['b'] = 4
costs['c'] = 7
costs['d'] = infinity
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['с'] = 'start'
parents['d'] = None
parents['fin'] = None

processed = ['start']

def find_lowest_cost_node(costs):
    lowest_costs = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_costs and node not in processed:
            lowest_costs = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neigbors = graph[node]
    for n in neigbors.keys():
        new_cost = cost + neigbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

s = 'fin'
result = ['fin']
while s != 'start':
    a = parents[s]
    result.append(a)
    s = a
result.reverse()
print(result)



