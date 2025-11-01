
"""
SO Basically In loop A[n] value difine index but when work with n for [2,3,4] then first n valie defone 2 not 0m index
"""

A = [1, 2, 3, 4, 1]
for n in A:          #break point
    A[n] = 0
    print(A)


# myLists = [1, 2, 3, 4, 5]
# myLists[0] = 10
# for x in myLists:
#     print(x)


# 1 0 3 4 1
# 0 0 3 4 1
# 0 0 3 0 1
# 0 0 3 0 1
# 0 0 3 0 1