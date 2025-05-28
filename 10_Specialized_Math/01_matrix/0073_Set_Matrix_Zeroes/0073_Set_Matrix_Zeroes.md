# [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/)

## Problem Statement
एक 2D `matrix` दिला आहे. जर matrix मधील कुठलाही element `0` असेल, तर त्या पूर्ण row आणि column ला `0` करायचं आहे.

> Constraint:
> हे inplace/in-place (म्हणजे original matrix मध्येच) करायचं आहे.
> O(1) extra space वापरायचा आहे (optimal साठी).  

**Example**
```python
Input:
matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]

Output:
[
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
```
```python
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```
## Possible Solutions – Brute Force to Optimized
## 1) Brute Force Approach – Mark then Convert (O(m × n × (m + n)) Time, O(1) Space with Marker)
> idea:  
> प्रत्येक `0` साठी त्याचा row आणि column `0` करायचा, पण direct केलं तर पुढचा data corrupt होईल.
> म्हणून आधी `-1` kiva `'#'` ने mark करायचं आणि नंतर सगळी `-1/'#'` values `0` मध्ये convert करायच्या.
```python
rows, cols = len(matrix), len(matrix[0])
for i in range(rows):
  for j in range(cols):
    if matrix[i][j] == 0:  # Mark the entire row and col with a temp value (-1)
      for k in range(rows):
        if matrix[k][j] != 0: matrix[k][j] = -1
      for k in range(cols):
        if matrix[i][k] != 0: matrix[i][k] = -1

# Convert all -1 to 0
for i in range(rows):
  for j in range(cols):
    if matrix[i][j] == -1: matrix[i][j] = 0
```
## 2) Use Extra Space (O(m+n) Space)
> दोन arrays वापरू – एक `row[]`, एक `col[]`.  
> `matrix[i][j] == 0` असेल तर row[i] आणि col[j] ला mark कर.
> नंतर दुसऱ्या loop मध्ये, जर row[i] किंवा col[j] mark असेल तर matrix[i][j] = 0.  
```python
rows, cols = len(matrix), len(matrix[0])
row_mark = [False] * rows
col_mark = [False] * cols
    
for i in range(rows):
  for j in range(cols):
    if matrix[i][j] == 0:
      row_mark[i] = True
      col_mark[j] = True

for i in range(rows):
  for j in range(cols):
    if row_mark[i] or col_mark[j]: matrix[i][j] = 0

#एका row आणि col ची list तयार केली जी zero असलेल्या positions track करते. नंतर त्या positions वापरून final zero fill केलं.
```
## 3) Optimized - Use First Row & First Column as Markers (O(1) Extra Space)
> Idea: आपल्याला extra space न वापरता zero positions track करायचं आहे.   
> matrix चाच first row आणि first column वापरू markers म्हणून!  
> BUT: एक special flag लागेल: is_first_col_zero → कारण row 0 आणि col 0 दोन्ही common असतात.  

**Dry Run:**  
Step 1: Traverse full matrix  
> जर कुठे `matrix[i][j] == 0` असेल:  
> `matrix[i][0] = 0` # row marker  
> `matrix[0][j] = 0` # col marker

Step 2: Matrix traverse करताना marker check करून `0` fill कर.  
Step 3: शेवटी, जर `matrix[0][0]` किंवा `is_first_col_zero true` असेल, तर complete row `0` किंवा col `0` zero कर.

```python
rows, cols = len(matrix), len(matrix[0])
is_first_col_zero = False

# Step 1: Use first row & column as markers
for i in range(rows):
  if matrix[i][0] == 0: is_first_col_zero = True
  for j in range(1, cols):
    if matrix[i][j] == 0:
      matrix[i][0] = 0
      matrix[0][j] = 0

# Step 2: Fill zero using markers (excluding first row/col)
for i in range(1, rows):
  for j in range(1, cols):
    if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0

# Step 3: Handle first row
if matrix[0][0] == 0:
  for j in range(cols):
    matrix[0][j] = 0

# Step 4: Handle first column
if is_first_col_zero:
  for i in range(rows):
    matrix[i][0] = 0
```
