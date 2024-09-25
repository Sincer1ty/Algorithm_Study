import sys
input = sys.stdin.readline

# 도시의 개수
n = int(input())
# 도로의 개수
m = int(input())

# 노드 생성
class Node:
	def __init__(self, val):
		self.adj = []
		self.val = val
		self.distance = 0
		self.visited = 0

vertex = [None]
nodeFrom = [[0]] * (n+1)
for n in range(n):
	vertex.append(Node(n+1))

for _ in range(m):
    # 출발 도시, 도착 도시, 시간
    u, v, t = map(int, input().split())
    vertex[u].adj.append((vertex[v], t))

start, dest = map(int, input().split())

def dfs(v : Node):
	if v.visited == 1:
		return

	v.visited = 1
	
	for n, t in v.adj:
		if n.distance < v.distance+t:
			nodeFrom[n.val] = [v.val]
			n.distance = v.distance+t
		elif n.distance == v.distance+t:
			nodeFrom[n.val].append(v.val)
		dfs(n)

dfs(vertex[start])
# print(nodeFrom)
print(vertex[dest].distance)

count = 0
def countRoute(k):
	global count
	q = [k]
	while q:
		cur = q.pop(0)
		if nodeFrom[cur] != [0]:
			count += len(nodeFrom[cur])
			q.extend(nodeFrom[cur])

countRoute(dest)
print(count)
