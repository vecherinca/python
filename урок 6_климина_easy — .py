
# coding: utf-8

# In[7]:


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math
class T ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def per(self):
        
        self.per = (self.AB + self.BC + self.CA)
        return (self.per)

    def square(self):
        self.per /=2
        self.square =  round(math.sqrt(self.per*(self.per - self.AB)*(self.per - self.BC)* (self.per - self.CA)),2)
        return (self.square)

    def h(self):
        self.square *=2
        self.h =  round((self.square / self.CA),2)
        return (self.h)


# In[11]:


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
tri = T(4,5,7,6,7,9)


print('Длинна строны АВ = {}, ВС = {}, СА = {}'.format(tri.AB, tri.BC, tri.CA))
print('Периметр треугольника АВС равен {}'.format(tri.per()))
print('Площадь треугольника АВС равна {}'.format(tri.square()))

if 'AB'=='BC'=='CA':
    print('Трапеция равнобочная')
else:
    print('Трапеция не равнобочная')


# In[ ]:




