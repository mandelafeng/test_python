def find_incidents(start, adjacency_list):
    # 使用队列来支持广度优先搜索
    from collections import deque
    queue = deque([start])
    incidents_found = set()  # 存储发现突发情况的点

    while queue:
        current = queue.popleft()
        if current in incidents_found:
            continue

        # 假设我们可以调用一个函数来检测是否有突发情况
        if has_incident(current):
            incidents_found.add(current)
            # 添加相邻点到队列中
            for neighbor in adjacency_list[current]:
                queue.append(neighbor)

    return incidents_found


def has_incident(point):
    # 这是一个模拟函数，实际中需要接入监控系统的API
    # 假设点3, 4, 5有突发情况
    return point in {3, 4, 5}


# 构建一个简单的相邻列表表示图
adjacency_list = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6],
    6: [5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8, 10],
    10: [9]
}

# 从点3开始检测
incident_points = find_incidents(3, adjacency_list)
print("监控到的突发情况点：", incident_points)