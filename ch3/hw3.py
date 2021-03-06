"""
1. The elements of a list are mutable whereas the elements of a tuple are immutable.
2. When we do not want to change the data over time, the tuple is a preferred data type whereas when we need to change the data in future, list would be a wise option.
3. Iterating over the elements of a tuple is faster compared to iterating over a list.
4. Elements of a tuple are enclosed in parenthesis whereas the elements of list are enclosed in square bracket.
"""

'''Q1: 
find the odd numbers in data1 and represents as a set odd. print(odd)'''
data1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even = {2, 4, 6, 8, 10}
odd = data1.difference(even)
print(set(odd))


'''Q2:
find the index of '歡樂水' in data2 and print '歡樂水', print(data2...)'''
data2 = ('moda', ('走', '了'), ('買', '肥宅', '歡樂水'))
print(data2[2][2])


#Q3:
#3.1 計算data3所有數字的總和
data3 = {39, 12, 61, 10, 3, 99, 78, 87, 93, 11, 666, 999}
print(sum(data3))
#3.2 找出data3內最大的數字, data3_max, 及最小的數字 data3_min, print(data3_max), print(data3_min)
data3 = {39, 12, 61, 10, 3, 99, 78, 87, 93, 11, 666, 999}
data3_max = max(data3)
data3_min = min(data3)
print(data3_max)
print(data3_min)
#3.3 分別將 data3 的數字由大到小排序 print(data_desc), 由小到大排序 print(data_asc)
data3 = {39, 12, 61, 10, 3, 99, 78, 87, 93, 11, 666, 999}
data_desc = sorted(data3,reverse=True)
data_asc = sorted(data3)
print(data_desc)
print(data_asc)

#Q4:
#4.1 將'moda'換成'米血', 並將data4 轉成字串, 印出 '米血走了~ 買肥宅歡樂水'
data4 = ['moda', '走', '了', '~ ', '買', '肥宅', '歡樂水']
data4[0] = '米血'
data4_new1 = ''.join(data4)
print(data4_new1)
#4.2 將data4轉成字串, 順序跟原本的data4相反, 印出 '歡樂水肥宅買~ 了走moda
data4 = ['moda', '走', '了', '~ ', '買', '肥宅', '歡樂水']
data4_new2 = ''.join(data4[::-1])
print(data4_new2)