import matplotlib.pyplot as plt
import numpy as np


x = plt.subplot(2, 3, 1)
x.plot(np.random.random(10))
y = plt.subplot(2, 3, 2)
y.plot(np.random.random(10))
z = plt.subplot(2, 3, 3)
z.plot(np.random.random(10))
n = plt.subplot(2, 1, 2)
n.plot(np.arange(0, 5, 0.5), '*-', label='концентрация', color='b')
n.legend()

plt.suptitle('Графики', fontsize=25, color='g')

x.grid()
y.grid()
z.grid()
n.grid()

plt.show()
#

# Библиотека numpy

a = np.array([3,5,7])
a_multiplication = a * 5 # Умножение массива на число
print(f'a = {a}')
print(f'a_multiplication={a_multiplication}')
print(a.size)  # выводит кол-во элементов массива a

# Создаем массивы из целых случайных чисел
b = np.random.randint(15, size=2)
c = np.random.randint(1, 10, size=3)

print(f'b = {b}')
print(f'c = {c}')

#  Перемножаем матрицы

d = np.arange(1, 10).reshape(3, 3)
print(f'd = {d}')
k = np.dot(a, d)  # Умножаем вектор на матрицу
i = np.dot(d, a)  # Умножаем матрицу на вектор

print(f'x = {k}')

print(f'y = {i}')



# matplotlib

#создаем 3 координатных оси и 3 графика со случайными значениями
