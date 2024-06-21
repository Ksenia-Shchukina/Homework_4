import random

from math import pi


def test_greeting():
    name = "Анна"
    age = 25
    output = f'Привет, {name}! Тебе {age} лет.'
    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)


def test_rectangle():
    a = 10
    b = 20
    perimeter = (a + b) * 2
    assert perimeter == 60
    area = a * b
    assert area == 200


def test_circle():
    r = 23
    area = pi * r**2
    assert area == 1661.9025137490005
    length = 2 * pi * r
    assert length == 144.51326206513048
    print(f'{area=}')
    print(f'{length=}')


def test_random_list():
    list_numbers = random.sample(range(1, 101), 10)
    list_numbers.sort()
    assert len(list_numbers) == 10
    assert all(list_numbers[i] <= list_numbers[i + 1] for i in range(len(list_numbers) - 1))


def test_unique_elements():
    list_numbers = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    list_numbers = list(set(list_numbers))
    assert isinstance(list_numbers, list)
    assert len(list_numbers) == 10
    assert list_numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    d = dict(zip(first, second))
    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
