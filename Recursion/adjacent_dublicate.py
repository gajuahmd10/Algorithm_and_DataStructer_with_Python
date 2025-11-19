def hasAdjacent(str, i=1):
    if i>=len(str):
        return True
    elif str[i] == str[i-1]:
        print(str[i] + str[i])
    else:
        return hasAdjacent(str, i+1)
hasAdjacent("programming")



#iterative one

# def check_Adjacence(str):
#     for i in range (len(str)):
#         if str[i] == str[i-1]:
#             return True
#
#     return False
# b = check_Adjacence("Apple")
# print(b)