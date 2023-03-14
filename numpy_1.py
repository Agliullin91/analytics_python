import numpy as np
from numpy import linalg


# Задание 1
# Создайте numpy array с элементами от числа N до 0. Например,
# для N = 10 это будет array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])).


def create_array(start, end, stride):
    return np.arange(start, end, stride)

# Задание 2
# Создайте диагональную матрицу с элементами от N до 0. Посчитайте сумму её значений на диагонали.


def create_matrix(start, end, stride):
    return np.diag(np.arange(start, end, stride))

# Задание 3
# Решите систему уравнений:
# 4x + 2y + z = 4
# x + 3y = 12
# 5y + 4z = -3


def task_3():
    left_side = np.array([[4, 2, 1], [1, 3, 0], [0, 5, 4]])
    right_side = np.array([4, 12, -3])
    result = linalg.solve(left_side, right_side)
    return result

# Задание 4
# Задание и входные данные к нему находятся в материалах занятия: ноутбук к лекции «Библиотека NumPy. Вычислительные
# задачи» ---- Python_9_Numpy.ipynb ---- Косинусное сходство между векторами ---- Задача 4 домашнего задания.


def find_similar(user_stats, new_user_stats):
    nus_len = np.linalg.norm(new_user_stats)
    cos_list = []
    for num, element in enumerate(user_stats):
        element_len = np.linalg.norm(element)
        cos = np.dot(element, new_user_stats) / (element_len * nus_len)
        cos_list.append((num, cos))
    cos_list.sort(key=lambda x: x[1], reverse=True)
    return cos_list[0]


if __name__ == '__main__':
    print(create_array(0, 10, 2))
    print(create_matrix(2, 20, 3))
    print(task_3())

    users_stats = np.array(
        [
            [2, 1, 0, 0, 0, 0],
            [1, 1, 2, 1, 0, 0],
            [2, 0, 1, 0, 0, 0],
            [1, 1, 2, 1, 0, 1],
            [0, 0, 1, 2, 0, 0],
            [0, 0, 0, 0, 0, 5],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 3],
            [1, 0, 0, 2, 1, 4]
        ],
        np.int32
    )

    next_user_stats = np.array([0, 1, 2, 0, 0, 0])

    print(find_similar(users_stats, next_user_stats))


