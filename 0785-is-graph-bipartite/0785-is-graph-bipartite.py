class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        color = [0] * n
        for i in range(n):
            if color[i] == 0:
                stack = [i]
                color[i] = 1
                while stack:
                    u = stack.pop()
                    for v in graph[u]:
                        if color[v] == 0:
                            color[v] = -color[u]
                            stack.append(v)
                        elif color[v] == color[u]:
                            return False
        return True

        