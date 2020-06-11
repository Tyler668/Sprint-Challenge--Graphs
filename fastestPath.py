from graph import Queue, Stack, Graph
import ast

filepath = "C:\\Users\\tyler\\Documents\\github\\Sprint-Challenge--Graphs\\maps\\main_maze.txt"

f = open(filepath, 'r')
# answer = {}
# for line in f:
#     k, v = line.strip().split(':')
#     answer[k.strip()] = v.strip()

# f.close()

with open(filepath, 'r') as file:
    data = file.read().replace('\n', '')
    # data = file.read().replace('\n', '')
mazeDict = ast.literal_eval(data)


print(mazeDict)
mazeGraph = Graph()


for key, value in mazeDict.items():
    mazeGraph.add_vertex(key)
    # print('---')
    for key2, value2 in dict(value[1]).items():
        # print(value2)
        if key in mazeGraph.vertices and value2 in mazeGraph.vertices:
            mazeGraph.add_edge(key, value2)
            mazeGraph.add_edge(value2, key)

# print('\n\n')

print('Vertices:', mazeGraph.vertices)
