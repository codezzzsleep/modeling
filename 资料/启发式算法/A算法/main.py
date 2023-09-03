import heapq
import numpy as np


class Node:
    def __init__(self, position, g_cost, h_cost):
        self.position = position
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.parent = None

    def __lt__(self, other):
        return self.f_cost < other.f_cost


def compute_h_cost(position, goal):
    return abs(goal[0] - position[0]) + abs(goal[1] - position[1])


def reconstruct_path(current_node):
    path = []
    while current_node.parent is not None:
        path.append(current_node.position)
        current_node = current_node.parent
    path.append(current_node.position)
    return path[::-1]


def get_neighbors(position, cost_map, closed_set, goal):
    x, y = position
    neighbors = []

    for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x = x + delta_x
        new_y = y + delta_y

        if (
                0 <= new_x < cost_map.shape[0]
                and 0 <= new_y < cost_map.shape[1]
                and cost_map[new_x][new_y] != -1
                and (new_x, new_y) not in closed_set
        ):
            h_cost = compute_h_cost((new_x, new_y), goal)
            g_cost = cost_map[new_x][new_y]
            neighbors.append(Node((new_x, new_y), g_cost, h_cost))

    return neighbors


def a_star(start, goal, cost_map):
    open_set = []
    closed_set = set()

    start_node = Node(start, 0, compute_h_cost(start, goal))

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(current_node.position)

        if current_node.position == goal:
            return reconstruct_path(current_node)

        neighbors = get_neighbors(current_node.position, cost_map, closed_set, goal)

        for neighbor in neighbors:
            tentative_g_cost = current_node.g_cost + neighbor.g_cost
            neighbor_exists = False
            for node in open_set:
                if node.position == neighbor.position:
                    if node.g_cost > tentative_g_cost:
                        node.g_cost = tentative_g_cost
                        node.f_cost = node.g_cost + neighbor.h_cost
                        node.parent = current_node
                    neighbor_exists = True
                    break
            if not neighbor_exists:
                neighbor.parent = current_node
                heapq.heappush(open_set, neighbor)
    return None


if __name__ == "__main__":
    cost_map = np.array(
        [
            [0, 0, 0, 0, 0],
            [0, -1, -1, -1, 0],
            [0, -1, 0, 0, 0],
            [0, -1, -1, -1, 0],
            [0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )

    start = (0, 0)
    goal = (5, 4)

    path = a_star(start, goal, cost_map)

    if path is not None:
        print("找到的路径:", path)
    else:
        print("找不到路径")
