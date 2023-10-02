x = 1
y = 1
z = 1
n = 2

print(
    [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
)
# explain the code
# 1. range(x+1) = [0,1]
# 2. range(y+1) = [0,1]
# 3. range(z+1) = [0,1]
# 4. if i + j + k != n
#    1 + 0 + 0 != 2
#    0 + 1 + 0 != 2
#    0 + 0 + 1 != 2
#    1 + 1 + 0 != 2
#    1 + 0 + 1 != 2
#    0 + 1 + 1 != 2
#    1 + 1 + 1 != 2
#    [0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,1,0],[1,0,1],[0,1,1]
# 5. print the result
