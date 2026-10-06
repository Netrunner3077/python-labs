# Python Labs

Лабораторные работы по дисциплине «Программирование на Python».
Магистратура «Цифровое Востоковедение», ДГТУ, 2026.

**Студент:** Токарев В.С., группа МЛ12
**Преподаватель:** доц. Швидченко С.А.
**Вариант:** 14

## Структура

| Папка                     | Тема                     | Задание                                                  |
| ------------------------- | ------------------------ | -------------------------------------------------------- |
| `lab_01_linear_function/` | Линейный алгоритм        | Вычислить `u = (x·e^(xy) + 4·cos²x) / (x·(x−y)·(2x+y))`  |
| `lab_02_branching/`       | Разветвляющийся алгоритм | Кусочно-заданная функция (3 ветви)                       |
| `lab_03_loops/`           | Циклы                    | Табуляция + сумма `y > 0` на `[−5; 5]`, шаг 0.4          |
| `lab_04_arrays/`          | Массивы                  | Массив 90 элементов → матрица 10×9, номера положительных |

## Установка

```bash
git clone <repo-url>
cd python-labs
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
# .venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Запуск

```bash
python lab_01_linear_function/src/calculate_function_lab_01_v14_(advanced).py
python lab_01_linear_function/src/calculate_function_lab_01_v14_(basic).py
python lab_01_linear_function/examples/randomizer.py

python lab_02_branching/src/cbranching_lab_02_v14_(advanced).py
python lab_02_branching/src/branching_lab_02_v14_(basic).py

python lab_03_loops/src/tabulation_sum_lab_03_v14_(advanced).py
python lab_03_loops/src/tabulation_sum_lab_03_v14_(basic).py

python lab_04_arrays/src/array_positive_indices_lab_04_v14_(advanced).py
python lab_04_arrays/src/array_positive_indices_lab_04_v14_(basic).py
# ... и т.д.
```

## Или через Makefile:

```bash
make lab1-basic
make lab1-advanced
make test
# ... и т.д.
```

## Тестирование

```bash
pytest
```
