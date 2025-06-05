# [1061. Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/)

## Problem Statement
You are given two strings `s1` and `s2` of the same length, and another string `baseStr`. Characters `s1[i]` and `s2[i]` are considered equivalent.

Using these equivalences, any characters related directly or indirectly are grouped together. Your task is to transform each character in `baseStr` into the lexicographically smallest character in its equivalence group and return the resulting string.

**Rules for equivalence:**

* Reflexivity: Every character is equivalent to itself.
* Symmetry: If 'a' == 'b', then 'b' == 'a'.
* Transitivity: If 'a' == 'b' and 'b' == 'c', then 'a' == 'c'.

## Example
```python
Input: s1 = "parker", s2 = "morris", baseStr = "parser"
Output: "makkek"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
The characters in each group are equivalent and sorted in lexicographical order.
So the answer is "makkek".

Input: s1 = "hello", s2 = "world", baseStr = "hold"
Output: "hdld"
Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".

Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
Output: "aauaaaaada"
Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
```

---

# 1. Union-Find (Disjoint Set) - Classic Approach
## Step-by-Step Approach:
1. **First, create a `parent` list of size 26 where each character is its own parent initially (`parent[i] = i`)**
   – This sets up the Union-Find structure for all lowercase letters `'a'` to `'z'`.

2. **Then define a `find(x)` function to find the root parent of character `x`**
   – It uses **path compression** for efficiency so that future `find` calls are faster.

3. **Define a `union(a, b)` function to group two characters `a` and `b`**
   – This merges their parent groups by always keeping the **lexicographically smaller character** as the parent (i.e., the one with the smaller index).

4. **Loop through pairs of characters from `s1` and `s2`, and `union(ord(a)-97, ord(b)-97)`**
   – This builds equivalence classes using Union-Find by linking characters based on their relationships.

5. **Finally, for each character `c` in `baseStr`, find its smallest equivalent using `find()` and build the result**
   – Convert the parent index back to character using `chr(find(ord(c)-97)+97)` and join them into the final string.

```python
def smallestEquivalentString(s1, s2, baseStr):
    parent = list(range(26))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            if pa < pb: parent[pb] = pa
            else: parent[pa] = pb
    for a, b in zip(s1, s2):
        union(ord(a)-97, ord(b)-97)
    return ''.join(chr(find(ord(c)-97)+97) for c in baseStr)
```

* **Time:** O(N α(26)) \~ O(N), N = length of s1/s2/baseStr
* **Space:** O(1) (fixed alphabet size)

---

# 2. Union-Find with Path Compression (Recursive Find)
## Step-by-Step Approach:
1. **First, create a list `parent = [0, 1, 2, ..., 25]` to represent each character 'a' to 'z' as its own parent**
   – This initializes the Union-Find structure.

2. **Define the `find(x)` function with path compression:**
   – If `x` is not its own parent, recursively find its root and update `parent[x]` to point directly to the root.
   – This helps flatten the structure for efficiency.

3. **Define the `union(a, b)` function to merge the groups of characters `a` and `b`:**
   – Find their parents `pa` and `pb`.
   – Attach the larger one to the smaller one to ensure lexicographical order.

4. **Loop through each character pair from `zip(s1, s2)` and perform union operation:**
   – This builds equivalence groups across all characters based on their relations.

5. **Construct the final string:**
   – For each character `c` in `baseStr`, find its smallest equivalent using `find`, convert it back using `chr(...)`, and join all characters to form the result.

```python
def smallestEquivalentString(s1, s2, baseStr):
    parent = list(range(26))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(a,b):
        pa, pb = find(a), find(b)
        if pa != pb:
            if pa < pb: parent[pb] = pa
            else: parent[pa] = pb
    for a,b in zip(s1,s2):
        union(ord(a)-97, ord(b)-97)
    return ''.join(chr(find(ord(c)-97)+97) for c in baseStr)
```
* Same complexity as above, different find style.

---

# 3. Union-Find Using `map` and `lambda`
## Step-by-Step Approach:
1. **First, create a parent list `p = [0, 1, ..., 25]` to represent each character 'a' to 'z'**
   – Each character is initially its own group.

2. **Define a lambda function `f(x)` for the find operation:**
   – It returns the root parent of `x`.
   – No path compression here, but still functional for small character set.

3. **Define a `u(a, b)` function to union characters `a` and `b`:**
   – It finds the root parents `pa` and `pb`.
   – Sets the lexicographically larger root to point to the smaller one.

4. **Loop over pairs of characters in `zip(s1, s2)` and apply union:**
   – This builds connected equivalence groups.

5. **For each character `c` in `baseStr`, find its smallest equivalent via `f`, convert back to char, and join:**
   – This generates the lexicographically smallest equivalent string.

```python
def smallestEquivalentString(s1, s2, baseStr):
    p = list(range(26))
    f = lambda x: x if p[x]==x else f(p[x])
    def u(a,b):
        pa, pb = f(a), f(b)
        if pa != pb:
            if pa < pb: p[pb] = pa
            else: p[pa] = pb
    for a,b in zip(s1,s2): u(ord(a)-97, ord(b)-97)
    return ''.join(chr(f(ord(c)-97)+97) for c in baseStr)
```
* Functional style, similar complexity.

---

# 4. Using Arrays + BFS to Find Groups and Map to Lex Smallest
## Step-by-Step Approach:
1. **First, build a graph using `defaultdict(set)` from `s1` and `s2`**
   – Each pair `(a, b)` implies an undirected connection: `a == b`.
   – So add both `graph[a].add(b)` and `graph[b].add(a)`.

2. **Initialize `visited` set and `char_map` dictionary**
   – `visited` keeps track of characters already processed.
   – `char_map` will map each character to its smallest equivalent.

3. **Then for each unvisited character in the graph, do BFS using a queue `q`**
   – Collect all characters in the connected group using BFS.
   – This gives the full equivalence class for that component.

4. **Find the lexicographically smallest character `mn` in the group**
   – Assign it as the representative of the group in `char_map`.

5. **Finally, build and return the result string**
   – For each character `c` in `baseStr`, replace it with `char_map[c]` if exists; otherwise keep it unchanged.

```python
from collections import defaultdict, deque
def smallestEquivalentString(s1, s2, baseStr):
    graph = defaultdict(set)
    for a,b in zip(s1,s2):
        graph[a].add(b)
        graph[b].add(a)
    visited = set()
    char_map = {}
    for c in graph:
        if c not in visited:
            q = deque([c])
            group = []
            while q:
                x = q.popleft()
                if x not in visited:
                    visited.add(x)
                    group.append(x)
                    q.extend(graph[x]-visited)
            mn = min(group)
            for ch in group:
                char_map[ch] = mn
    return ''.join(char_map.get(c,c) for c in baseStr)
```
* **Time:** O(N) + BFS over at most 26 chars
* **Space:** O(26)

---

# 5. Using DFS to Find Connected Components and Map to Smallest
## Step-by-Step Approach:
1. **First, build a graph `g` using `defaultdict(set)` from pairs in `s1` and `s2`**
   – For each `(a, b)` in `zip(s1, s2)`, add `b` to `g[a]` and `a` to `g[b]`.
   – This models equivalence relationships between characters.

2. **Initialize `visited` set and `rep` dictionary**
   – `visited` tracks all characters already explored.
   – `rep` will store the smallest representative character for each group.

3. **Then for each unvisited character in `s1 + s2`, run DFS**
   – `dfs(c, comp)` collects all connected characters starting from `c` into the set `comp`.
   – This builds a full equivalence class of connected nodes.

4. **Find the smallest character `mn` in each component `comp`**
   – Assign `mn` as the representative for all characters in `comp` by updating `rep`.

5. **Finally, return the new string**
   – For each character in `baseStr`, replace it with its representative from `rep`, or keep it unchanged if not found.

```python
from collections import defaultdict
def smallestEquivalentString(s1, s2, baseStr):
    g = defaultdict(set)
    for a,b in zip(s1,s2):
        g[a].add(b)
        g[b].add(a)
    visited = set()
    rep = {}
    def dfs(c, comp):
        comp.add(c)
        for nei in g[c]:
            if nei not in comp:
                dfs(nei, comp)
    for c in set(s1+s2):
        if c not in visited:
            comp = set()
            dfs(c, comp)
            mn = min(comp)
            for x in comp:
                rep[x] = mn
            visited |= comp
    return ''.join(rep.get(c,c) for c in baseStr)
```
* DFS variant of BFS solution.

---

# 5A. DFS per character on the graph without precomputing components
## Step-by-Step Approach:
1. **First, build the undirected graph using `adj[a].append(b)` and `adj[b].append(a)`**
   – Each character in `s1[i]` and `s2[i]` is treated as connected (equivalent).
   – This sets up a graph where connected components represent equivalence classes.

2. **Then, define a recursive DFS function `dfs(ch, visited)`**
   – It explores all characters connected to `ch` and returns the lexicographically smallest one in that component.
   – It keeps track of visited characters to avoid cycles.

3. **Now for each character `ch` in `baseStr`, run `dfs(ch, visited)`**
   – This finds the smallest equivalent character for `ch` from its connected component.

4. **Collect all results in a list `result` and finally return `''.join(result)`**
   – This forms the lexicographically smallest equivalent string.

```python
from collections import defaultdict
class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
      adj = defaultdict(list)
      for a, b in zip(s1, s2):
         adj[a].append(b)
         adj[b].append(a)

      def dfs(ch, visited):
         visited.add(ch)
         min_ch = ch
            for nei in adj[ch]:
               if nei not in visited:
                  candidate = dfs(nei, visited)
                  min_ch = min(min_ch, candidate)
         return min_ch

      result = []
      for ch in baseStr:
         visited = set()
         result.append(dfs(ch, visited))
        
      return ''.join(result)
```
* **Time:** O(N × 26), where N = len(baseStr) (each DFS can visit all 26 lowercase letters in worst case).
* **Space:** O(26 + N) for the graph and visited set.

---

# 6. Using `defaultdict` + Iterative Union-Find with `find` caching in dict
## Step-by-Step Approach:
1. **First, initialize the `parent` dictionary with each lowercase letter mapping to itself**
   – This means initially each character is its own representative in the union-find structure.

2. **Then define the `find(c)` function with path compression**
   – It returns the root representative of character `c`.
   – While traversing up the parent chain, it flattens the structure for efficiency.

3. **Define the `union(a, b)` function to join two character groups**
   – Find the leaders `pa` and `pb` of `a` and `b`.
   – Link the lexicographically larger group to the smaller one to preserve minimal character as root.

4. **Now process every pair `(a, b)` from `zip(s1, s2)` with `union(a, b)`**
   – This forms all equivalence groups among characters.

5. **Finally, return the result string**
   – For every character in `baseStr`, use `find(c)` to get the smallest equivalent character.

```python
def smallestEquivalentString(s1, s2, baseStr):
    parent = {chr(c): chr(c) for c in range(97,123)}
    def find(c):
        while parent[c] != c:
            parent[c] = parent[parent[c]]
            c = parent[c]
        return c
    def union(a,b):
        pa, pb = find(a), find(b)
        if pa != pb:
            if pa < pb: parent[pb] = pa
            else: parent[pa] = pb
    for a,b in zip(s1,s2): union(a,b)
    return ''.join(find(c) for c in baseStr)
```

---

# 7. Lambda + One-liner Union-Find (More Compact)
## Step-by-Step Approach:
1. **First, initialize the parent array `p` as `p = list(range(26))`**
   – This treats each lowercase letter (`'a'` to `'z'`) as its own group initially.

2. **Then define a one-liner `find` function `f(x)` using a lambda**
   – This recursively finds the representative (leader) of a character group.
   – No explicit path compression, but works for correctness.

3. **Define a compact `union` function `u(a, b)` as a lambda**
   – If roots of `a` and `b` differ, it sets both to the smaller one using `p.__setitem__()`
   – This enforces lexicographical minimal root across unions.

4. **Now for each pair in `zip(s1, s2)`**, perform `union()` using the character indices (`ord(ch)-97`)
   – This merges all equivalence classes accordingly.

5. **Finally, return the transformed baseStr**
   – For each character in `baseStr`, convert it to the index, find its group leader, and get the corresponding character via `chr(...)`.

```python
def smallestEquivalentString(s1, s2, baseStr):
    p = list(range(26))
    f = lambda x: x if p[x]==x else f(p[x])
    u = lambda a,b: (p.__setitem__(f(a), min(f(a), f(b))) or p.__setitem__(f(b), min(f(a), f(b)))) if f(a) != f(b) else None
    for a,b in zip(s1,s2): u(ord(a)-97, ord(b)-97)
    return ''.join(chr(f(ord(c)-97)+97) for c in baseStr)
```

---

## Summary Table

| Solution                       | Time Complexity | Space Complexity | Style                 | Best for Interviews?        |
| ------------------------------ | --------------- | ---------------- | --------------------- | --------------------------- |
| 1. Union-Find (Iterative find) | O(N)            | O(1)             | Clean & efficient     | ✅ Highly recommended        |
| 2. Union-Find (Recursive find) | O(N)            | O(1)             | Recursive style       | ✅ Recommended               |
| 3. Union-Find (Lambda style)   | O(N)            | O(1)             | Functional style      | Good for variety            |
| 4. BFS Graph Grouping          | O(N)            | O(1)             | Graph BFS approach    | Less common in interviews   |
| 5. DFS Graph Grouping          | O(N)            | O(1)             | Graph DFS approach    | Less common                 |
| 6. Union-Find with dict keys   | O(N)            | O(1)             | Dictionary keys style | Good alternative            |
| 7. One-liner Union-Find        | O(N)            | O(1)             | Compact/obscure style | Not recommended for clarity |

---

**For interviews, Solution #1 or #2 (classic union-find) is best.**
They are clear, efficient, and widely understood.
