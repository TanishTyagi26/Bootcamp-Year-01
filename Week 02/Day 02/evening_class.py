# lst=[10,20,30,40,50]
# for i in lst:
#     print(i)

# lst1=[1,2]
# lst2=[4,5]
# for i in lst1:
#     for j in lst2 :
#         print(i,j)

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()

# lst=[10,20]
# lst1=[1,2]
# for i in lst:
#     for j in lst1:
#         print(i+j)

#____________table of 2__________________
# lst=[2]
# for i in lst:
#     for j in range (1,11):
#         # print(f" {i} X {j} = {i*j}")
#         print(i,"X" ,j ,"=", i*j ,)
    
#_______________tables from 2 to 5________________  
# lst=[2,3,4,5]
# for i in lst:
#     for j in range (1,11):
#         # print(f" {i} X {j} = {i*j}")
#         print(i,"X" ,j ,"=", i*j ,)
#     print()



# for i in range(2,4):
#     for j in range(1,11):
#         if i == j :
#             break
#         print(i,j)


#
# a=[2,3,4,5]
# res=[val**2 for val in a]
# print(res)


# a=[1,2,3,4,5]
# res=[val for val in a if val%2 == 0]
# print(res)

# b=[5,12,7,18,3,20]
# res=[val for val in b if val>=10 ]
# print(res)


# a=[i for i in range(10)]
# print(a)


# c=[(x,y) for x in range(3) for y in range(3)]
# print(c)

# mat=[[1,2,3],[4,5,6],[7,8,9]]
# res=[val for row in mat for val in row]
# print(res)

# wap to modify the mutltiplication program so that it skips the multiple of 5 using continue
# lst=[2]
# for i in lst:
#     for j in range (1,51):
#         if j%5==0:
#             continue
#         print(f" {i} X {j} = {i*j}")



# for row in range(no.of rows):
#   for cols in range(no. of cols):
#       print("*", end=" ")
#    print()

# print('*')
# print('*')
# print('*')


#================== Square Pattern========================
# for i in range(4):
#     for j in range(4):
#         print("*",end=' ')
#     print()

#================== Rectangle Pattern========================

# for i in range(3):
#     for j in range(8):
#         print("*",end=' ')
#     print()

#================== Pyramid Pattern========================
# print("\n")
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=' ')
#     print()

#================== Inverted Pyramid Pattern========================

# for i in range(6,0,-1):
#     for j in range(i):
#         print("*",end=' ')
#     print()

#================== Full Pyramid Pattern========================
for i in range(5):
    for j in range(5,0,-1):
        print("*",end=' ')
    print()



#================== Diamond Pattern========================










