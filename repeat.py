# import random
# import timeit
#
#
# array = range(1,1000000000)
# x = """def swap1():
#
#     max_num = max(array)
#     min_num = min(array)
#     max_idx = array.index(max_num)
#     min_idx = array.index(min_num)
#     array[max_idx],array[min_idx] = min_num,max_num"""
# print(timeit.timeit(stmt=x,number=10))
#
# y = """def swap1():
#     max_num = max(array)
#     min_num = min(array)
#     for i in range(len(array)):
#         if array[i] == max_num:
#             array[i] == min
#         elif array[i] == min_num:
#             array[i] = max_num"""
# print(timeit.timeit(stmt=y,number=10))
#
#
#
# # Mytable - list,set,dict
# # Immutable - digits,str,bool,tuble,frozenset
#
# list1 = [4,100,-1,0]
# j = 0
# while j < len(list1)-1:
#     for i in range(len(list1)-1):
#         if list1[i] > list1[i+1]:
#             list1[i],list1[i+1] = list1[i+1],list1[i]
#     j +=1
#
# print(list1)
#
#
# list2 = [1,2,3,4,5]
# def fun(i):
#     i += 100
#     return i
# a = list(map(fun,list2))
# print(a)
#
#
# list2 = [random.randint(1,10000) for i in range(100000)]
# def fun(i):
#     list2 = [i for i in list2 if i >= 9000]
#
#
# names = ['maksimka','sanjar','rus','rasul','atai','erzhan']
# list2 = [random.randint(1,10000) for i in range(100000)]
# list3 = [random.choice(names) for i in range(100000)]
#
# a = list(zip(list3,list2))
# print(a)
#

data = [20,[144,213,-9],'urmat','beksultan']
def updateElem(elem):
    count = 0
    if isinstance(elem,list):
        for i in elem:
            count +=i
        return count
    elif isinstance(elem,str):
        elem = elem.capitalize()
        return elem
    elif isinstance(elem,int):
        return None
print(list(map(updateElem,data)))


