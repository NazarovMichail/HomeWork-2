# Проект 0. Угадай число
<img alt="logo" src="img/pylogo.jpg">

## `Оглавление`
[1. Описание проекта](https://github.com/NazarovMichail/HomeWork-2#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/NazarovMichail/HomeWork-2#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/NazarovMichail/HomeWork-2#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/NazarovMichail/HomeWork-2#Этапы-работы-над-проектом)

[5. Результат](https://github.com/NazarovMichail/HomeWork-2#Результаты)

[6. Выводы](https://github.com/NazarovMichail/HomeWork-2#Выводы)

### `Описание проекта`
___
Угадать загаданное компьютером число за  число попыток **меньше 20**.

:arrow_up:[к оглавлению](https://github.com/NazarovMichail/HomeWork-2#Оглавление)


### `Какой кейс решаем?`
___
Нужно написать программу, которая угадывает число за число попыток **меньше 20**.

**Условия соревнования:**
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**
Результаты оцениваются по среднему количеству попыток при 10000 повторений

**Что практикуем**
Учимся писать хороший код на python


### `Краткая информация о данных`
___
Предаставлен архив с базовым решением задачи.
**В архиве**:
- Ноутбук `game.ipynb` для демонстрации результата работы разработанной функции
- Файл `game.py` с примером случайного угадывания числа
- Файл `game_v2.py` с примером функции случайного угадывания числа и функции подсчета среднего количества угадываний
- Файл `README.md` с шаблоном описания работы программы

:arrow_up:[к оглавлению](https://github.com/NazarovMichail/HomeWork-2#Оглавление)


### `Этапы работы над проектом`
___
1) Фиксируем зависимости в файле `requirements.txt`.
2) Реализуем функцию бинарного поиска для угадывания слуайного числа в файле `game_v3.py`.
3) Тестируем функцию в ноутбуке `game.ipynb`.
4) Описываем всю информацию о проекте и результатах в файле `README.md`.
5) Отправляем все рабочие файлы в `GitHub`.

:arrow_up:[к оглавлению](https://github.com/NazarovMichail/HomeWork-2#Оглавление)


### `Результаты:`
___
Разработанная функция, которая использует алгоритм `бинарного поиска`, находит случайное число в среднем за **`5 попыток`** из `10000 измерений`.

:arrow_up:[к оглавлению](https://github.com/NazarovMichail/HomeWork-2#Оглавление)


### `Выводы:`
___
Временная сложность алгоритма бинарного поиска равна **`O(log2 n)`**, что при n = 100 позволяет достигнуть необходимого результата: количество попыток значительно меньше 20.

:arrow_up:[к оглавлению](https://github.com/NazarovMichail/HomeWork-2#Оглавление)
___


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
