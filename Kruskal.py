
departments = [
    "Computer", "IT", "Mechanical",
    "Civil", "Electrical", "Library"
]

V = len(departments)

# Edges: (Department1, Department2, Distance)
edges = [
    (0, 1, 10),  # Computer - IT
    (0, 2, 15),  # Computer - Mechanical
    (0, 3, 20),  # Computer - Civil
    (0, 5, 25),  # Computer - Library
    (1, 2, 35),  # IT - Mechanical
    (1, 4, 30),  # IT - Electrical
    (1, 5, 20),  # IT - Library
    (2, 3, 40),  # Mechanical - Civil
    (2, 4, 25),  # Mechanical - Electrical
    (3, 4, 15),  # Civil - Electrical
    (3, 5, 30),  # Civil - Library
    (4, 5, 10)   # Electrical - Library
]


# Create Adjacency Matrix
def create_adjacency_matrix():
    matrix = [[0 for _ in range(V)] for _ in range(V)]

    for u, v, weight in edges:
        matrix[u][v] = weight
        matrix[v][u] = weight

    return matrix


# Display Adjacency Matrix
def display_matrix():
    matrix = create_adjacency_matrix()

    print("\nAdjacency Matrix:\n")

    print(" " * 8, end="")

    for name in departments:
        print(f"{name[:8]:>10}", end="")

    print()

    for i in range(V):
        print(f"{departments[i]:8}", end="")

        for j in range(V):
            print(f"{matrix[i][j]:>10}", end="")

        print()


# Find Operation (Disjoint Set)
def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])

    return parent[vertex]


# Union Operation (Disjoint Set)
def union(parent, rank, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u == root_v:
        return False

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v

    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u

    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


# Kruskal's Algorithm
def kruskal():
    sorted_edges = sorted(edges, key=lambda x: x[2])

    parent = [i for i in range(V)]
    rank = [0] * V

    mst = []
    total_distance = 0

    for u, v, weight in sorted_edges:

        if union(parent, rank, u, v):
            mst.append((u, v, weight))
            total_distance += weight

        if len(mst) == V - 1:
            break

    return mst, total_distance


# Create Adjacency List
def create_adjacency_list():
    adjacency_list = [[] for _ in range(V)]

    for u, v, weight in edges:
        adjacency_list[u].append((v, weight))
        adjacency_list[v].append((u, weight))

    return adjacency_list


# Prim's Algorithm
def prim():
    adjacency_list = create_adjacency_list()

    selected = [False] * V
    mst = []
    total_distance = 0

    # Start from Computer department
    selected[0] = True

    while len(mst) < V - 1:

        minimum_weight = float("inf")

        selected_u = -1
        selected_v = -1

        for u in range(V):

            if selected[u]:

                for v, weight in adjacency_list[u]:

                    if not selected[v] and weight < minimum_weight:
                        minimum_weight = weight
                        selected_u = u
                        selected_v = v

        if selected_v == -1:
            break

        mst.append((selected_u, selected_v, minimum_weight))
        total_distance += minimum_weight

        selected[selected_v] = True

    return mst, total_distance


# Display Minimum Spanning Tree
def display_mst(mst, total_distance, algorithm):

    print("\n" + "=" * 60)
    print(algorithm)
    print("=" * 60)

    print(f"{'From':15}{'To':15}{'Distance (m)':15}")
    print("-" * 45)

    for u, v, weight in mst:
        print(
            f"{departments[u]:15}"
            f"{departments[v]:15}"
            f"{weight:<15}"
        )
    
    print("-" * 45)

    print("Total Minimum Distance =", total_distance, "meters")

    print("=" * 60)


# Main Program
print("=" * 60)
print("       COLLEGE CAMPUS MINIMUM SPANNING TREE")
print("=" * 60)

print("\nDepartments / Institutes:")

for i in range(V):
    print(i, "->", departments[i])


# Display Adjacency Matrix
display_matrix()


# Execute Kruskal's Algorithm
kruskal_mst, kruskal_total = kruskal()

display_mst(
    kruskal_mst,
    kruskal_total,
    "KRUSKAL'S ALGORITHM"
)


# Execute Prim's Algorithm
prim_mst, prim_total = prim()

display_mst(
    prim_mst,
    prim_total,
    "PRIM'S ALGORITHM"
)
