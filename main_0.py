# -*- coding: utf-8 -*-

# users that are connected in twitter and share at least one organization are added to the graph
import random
random.seed( 10 )

graph = {}
k = []
for i in range(2000):
    k.append([random.randint(0, 50),random.randint(0, 50)])

for i,j in k:

    if i != j:
        try:
            graph[i]
        except:
            graph.setdefault(i, [])

        if j not in graph[i]:
            graph[i].append(j)

        try:
            graph[j]
        except:
            graph.setdefault(j, [])

        if i not in graph[j]:
            graph[j].append(i)


def bron_kerbosch(r, p, x, graph, cliques):
    if not p and not x:
        cliques.append(r)
    else:
        for v in p.copy():
            bron_kerbosch(r.union([v]), p.intersection(graph[v]), x.intersection(graph[v]), graph, cliques)
            p.remove(v)
            x.add(v)
    return cliques


import time
time_start=time.time()
# find cliques for the given adjacency graph
cliques = bron_kerbosch(set(), set(graph.keys()), set(), graph, [])

time_end=time.time()
print(time_end-time_start)



# MIN_SIZE = 2
# filter out smaller cliques and sort users within each one alphabetically. Then, sort cliques by size
# cliques = filter(lambda s: len(s) >= MIN_SIZE, cliques)
# for i in enumerate(cliques):
#     cliques[i[0]] = sorted(i[1])
cliques = sorted(cliques, key=len, reverse=True)
print(len(cliques[0]))
print(cliques[0])