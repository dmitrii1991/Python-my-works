n = int(input())
graph = {}
data = []
data_test = []
for i in range(n):
    a = str(input())
    data.append(a)

n = int(input())
for i in range(n):
    a = str(input())
    data_test.append(a)

for line in data:
    if ':' in line:
        child, parents = line.split(' : ')
        for parent in parents.split(' '):
            if parent not in graph.keys():
                graph[parent] = [child]
            else:
                if child not in graph[parent]:
                    graph[parent].append(child)
    else:
        if line not in graph.keys():
            graph[line] = [line]


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        #print(visited, '--------------', stack)
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph.get(vertex, [vertex])) - set(visited))
    return visited

kk = 1
for i in data_test:
    for b in data_test[0:kk]:
        if i in dfs(graph, b):
            if i != b:
                print(i)
            break
    kk += 1
