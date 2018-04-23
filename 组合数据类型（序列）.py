# 组合数据类型：集合、序列（元组、列表）、字典

# 序列：有先后关系的一组元素，可以有相同元素，可根据编号访问元素
# 序列类型有字符串、元组、列表，其中元组和列表是组合数据类型
## 序列处理函数及方法（对元组和列表通用）
'''操作符'''
ls = ['python',1,2]
ls[::-1]
1 in ls
1 not in ls
ls + [1,2,3]
ls * 3
'''函数'''
len(ls)
min([1,2,3])    # 最小元素，前提是可比较，不可比较时报错（字符串比较字母序）
max([1,2,3])
ls.index(1)
ls.index(1,0,3)   # 序列ls中从第0到第3个位置中第一次出现元素1的位置
ls.count('python')   # 'python'出现的次数


# 元组：一旦创建，不能修改
a = (1,2,'hhh')
b = a,'rrr'
c = 4,6,6
a[::-1]
b[0][2]

# 列表：创建后可以随意更改
p = ['aa','b','ccc',1001]
f = list((1,2,3))
it = p     # 将同一个列表进行了两次赋值：p和it指向的是同一个列表（并没有新列表产生）
p[0] = 1     # 更改列表元素
p[1:3] = [9,8,7]    # 用[9,8,7]替换p中切片部分
del p[1]   # 删除元素
del p[:3:2]
p += f
p *= 6
## 列表的操作函数和方法
p.append('a')   # 在列表右侧增加元素
p.clear()    # 删除所有元素
p.copy()
p.insert(2,'zz')     # 在2号位置插入一个'zz'
p.pop()
p.remove('a')    # 删除列表中出现的第一个'a'
p.reverse()


'''
序列的应用场景：
1、数据表示
2、元组可用于数据保护，避免被改变
'''
