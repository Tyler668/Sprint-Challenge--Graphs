# Spent 2 hrs on this then ditched it, highly epic, don't read.


# from graph import Queue, Stack, Graph
# import ast

# filepath = "C:\\Users\\tyler\\Documents\\github\\Sprint-Challenge--Graphs\\maps\\main_maze.txt"

# f = open(filepath, 'r')

# with open(filepath, 'r') as file:
#     data = file.read().replace('\n', '')
# mazeDict = ast.literal_eval(data)


# # print(mazeDict)
# mazeGraph = Graph()


# for key, value in mazeDict.items():
#     mazeGraph.add_vertex(key)
#     # print('---')
#     for key2, value2 in dict(value[1]).items():
#         # print(value2)
#         if key in mazeGraph.vertices and value2 in mazeGraph.vertices:
#             mazeGraph.add_edge(key, value2)
#             mazeGraph.add_edge(value2, key)

# # print('\n\n')

# # print('Vertices:', mazeGraph.vertices.keys())

# # toExplore = list(mazeGraph.vertices.keys())
# # toExplore.sort()
# # print(toExplore)

# visited = {}
# # print('BFS', mazeGraph.bfs(494, 431))
# print('BFS Directory', mazeGraph.bfs_order(0))
# directions = mazeGraph.bfs_order(0)


# # print('Path:', mazeGraph.bfs_path(0, 268))
# path = []
# startNode = 0
# for i in range(len(directions)):

#     # if directions[i] in path:
#     #     i += 1

#     pieceOfPath = mazeGraph.bfs_path(startNode, directions[i])
#     pieceOfPath.pop(-1)

#     # print('Then this path:', path)
#     path += (pieceOfPath)
#     startNode = directions[i]

# print('Grand path:', path)

# print('Grand path length:', len(path))
