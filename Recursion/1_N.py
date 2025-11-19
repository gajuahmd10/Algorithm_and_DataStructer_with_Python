
""" All the function come after recursion line will execute once the recursion is completed"""
"""The function calls are stacked up (last-in, first-out)"""

                # !-- print 1 to n------!
# def execute_N(n):
#     if n==0:   #Based function
#        return None
#     print(n)
#     execute_N(n - 1)    #Hypothesis
#     print(n)   #indexing
#
# execute_N(7)



# def recursion(value):
#     if value==0:
#         return None
#     recursion(value - 1)
#     print(value)
# recursion(5)


            # !-----  N to 1----!
# def execute_N(n):
#     if n==0:   #Based function
#        return 1
#     print(n)  # indexing
#     execute_N(n - 1)    #Hypothesis
#
#
# execute_N(7)
#
# Best case print only one time
# else could work with 1 value
#  combine with Best case
# def execute_N(n):
#     if n==1:   #Based function
#        print(  1)
#     else:
#         print(n)
#         execute_N(n - 1)    #Hypothesis
#         print(n)   #indexing
#
# execute_N(7)