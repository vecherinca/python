
# coding: utf-8

# In[1]:


# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз


fruits=["яблоко", "банан", "киви", "арбуз"]
print('1.', fruits[0])
print('2.', fruits[1])
print('3.', fruits[2])
print('4.', fruits[3])


# In[2]:




# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok1=['white','black','green','orange']
spisok2=['blue','purple','yellow','orange']
for i in spisok1:
    for j in spisok2:
        if i == j:
            spisok1.pop(3)
            break
print(spisok1)


# In[6]:



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

num=[1,5,7,4,3,8,9,3,2]
new_list = []
for i in num:
    if i % 2 == 0:
        new_list.append(i * 4)
    else:
        new_list.append(i * 2)
print(new_list)


# In[5]:



