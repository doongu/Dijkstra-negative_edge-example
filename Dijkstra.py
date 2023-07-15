graph = {
    'A': {'B': -100, 'C': 10},
    'B': {'C': 10},
    'C': {}
}


import heapq

def dijkstra(graph, start):
  distances = {node: 1e9 for node in graph}  # start로 부터 '다른 node'의 거리 값을 저장하기 위함
  distances[start] = 0  # start에서 start의 거리는 0임
  queue = []
  heapq.heappush(queue, [distances[start], start])  # heapq를 통해 가장 가까운 거리의 노드를 선택

  while queue:  # queue에 더 살펴볼 node가 없다면 종료
    current_distance, current_destination = heapq.heappop(queue)  # 현재 바라보고 있는 노드에서
    # 가장 가까운 거리의 노드를 가져옴

    if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue

    new_nodes = graph[current_destination].items()
    
    for new_destination, new_distance in new_nodes:
      distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
      if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
        distances[new_destination] = distance
        heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
  return distances


print(dijkstra(graph, 'A'))