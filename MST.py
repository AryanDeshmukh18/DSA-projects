
d = ["Computer", "IT", "Mechanical", "Civil", "Electrical", "Library"]
V = len(d)
edges = [(0,1,10),(0,2,15),(0,3,20),(0,5,25),(1,2,35),
         (1,4,30),(1,5,20),(2,3,40),(2,4,25),(3,4,15),
         (3,5,30),(4,5,10)]

def matrix():
    m = [[0]*V for _ in range(V)]
    for u,v,w in edges: m[u][v] = m[v][u] = w
    print("\nAdjacency Matrix:\n")
    print(" "*8, end="")
    for x in d: print(f"{x[:8]:>10}", end="")
    print()
    for i in range(V):
        print(f"{d[i]:8}", end="")
        for x in m[i]: print(f"{x:>10}", end="")
        print()

def find(p, x):
    if p[x] != x: p[x] = find(p, p[x])
    return p[x]

def union(p, r, u, v):
    u,v = find(p,u),find(p,v)
    if u == v: return False
    if r[u] < r[v]: u,v = v,u
    p[v] = u
    if r[u] == r[v]: r[u] += 1
    return True

def kruskal():
    p, r, mst, total = list(range(V)), [0]*V, [], 0
    for u,v,w in sorted(edges, key=lambda x:x[2]):
        if union(p,r,u,v):
            mst.append((u,v,w)); total += w
            if len(mst) == V-1: break
    return mst,total

def prim():
    s, mst, total = [0], [], 0
    while len(s) < V:
        e = min((e for e in edges if (e[0] in s) != (e[1] in s)), key=lambda x:x[2])
        u,v,w = e
        mst.append(e); total += w
        s.append(v if u in s else u)
    return mst,total

def display(mst,total,name):
    print("\n"+"="*60+"\n"+name+"\n"+"="*60)
    print(f"{'From':15}{'To':15}{'Distance (m)':15}")
    print("-"*45)
    for u,v,w in mst: print(f"{d[u]:15}{d[v]:15}{w:<15}")
    print("-"*45)
    print("Total Minimum Distance =",total,"meters")
    print("="*60)

print("="*60+"\n       COLLEGE CAMPUS MINIMUM SPANNING TREE\n"+"="*60)
print("\nDepartments / Institutes:")
for i,x in enumerate(d): print(i,"->",x)

matrix()
display(*kruskal(),"KRUSKAL'S ALGORITHM")
display(*prim(),"PRIM'S ALGORITHM")
