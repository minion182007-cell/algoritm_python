# algoritm_python

[![tests](https://github.com/minion182007-cell/algoritm_python/actions/workflows/tests.yml/badge.svg)](https://github.com/minion182007-cell/algoritm_python/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/python-3.12-blue?logo=python&logoColor=white)
![Задач решено](https://img.shields.io/badge/задач_решено-3-brightgreen)
![Easy](https://img.shields.io/badge/easy-2-success)
![Medium](https://img.shields.io/badge/medium-1-orange)

Мои решения задач с [LeetCode](https://leetcode.com/) на Python. У каждой задачи есть код, тесты, разбор и скриншот принятого решения.

## Задачи

| № | Задача | Сложность | Решение | Время | Память |
|---|--------|-----------|---------|-------|--------|
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | 🟠 Medium | [сортировка](algos/medium/Find%20Minimum%20in%20Rotated%20Sorted%20Array/solution.py), [бинарный поиск](algos/medium/Find%20Minimum%20in%20Rotated%20Sorted%20Array/solution_binary_search.py) | O(log n) | O(1) |
| 599 | [Minimum Index Sum of Two Lists](https://leetcode.com/problems/minimum-index-sum-of-two-lists/) | 🟢 Easy | [решение](algos/easy/Minimum%20Index%20Sum%20of%20Two%20Lists/) | O(n + m) | O(n) |
| 709 | [To Lower Case](https://leetcode.com/problems/to-lower-case/) | 🟢 Easy | [решение](algos/easy/To%20Lower%20Case/) | O(n) | O(n) |

## Структура

```
algos/
├── easy/
│   └── <Название задачи>/
│       ├── README.md          # условие и разбор
│       ├── solution.py        # решение
│       ├── solution_*.py      # другие варианты решения (если есть)
│       ├── test_solution.py   # тесты, проверяют все варианты
│       └── picture.png        # скриншот принятого решения
└── medium/
    └── ...
```

## Запуск тестов

```bash
pip install -r requirements.txt
pytest -v
```

Тесты запускаются автоматически через GitHub Actions при каждом пуше.
