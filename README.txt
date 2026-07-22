Решение тестового задания по аналитике
======================================

Источник задания
----------------

  Analytic data.pdf

Состав проекта
--------------

  solutions/final_answers.txt
  Краткие ответы по всем блокам.

  solutions/block_1_probability_and_logic.txt
  Расчеты по теории вероятностей и логике.

  analytics_assignment/python_tasks.py
  Реализация трех функций из блока Python.

  solutions/block_2_python_complexity.txt
  Оценка сложности Python-решений.

  sql/examination_rank.sql
  SQL-запрос для рейтинга абитуриентов.

  sql/purchases_under_5000.sql
  SQL-запрос для клиентов с покупками меньше 5000 рублей за последний месяц.

  solutions/block_3_sql.txt
  Пояснения и ответ по FULL JOIN.

  solutions/block_4_statistics_ab_tests.txt
  Ответы по статистике и A/B-тестам.

  solutions/block_5_ml_base.txt
  Ответы и ручные расчеты по ML Base.

  analytics_assignment/calculations.py
  Проверочные функции для расчетов.

  analytics_assignment/report.py
  Скрипт печати итоговых числовых ответов.

  tests/test_python_tasks.py
  Unit-тесты для Python-задач и расчетов.

  tests/validate_project.py
  Проверка структуры, ключевых ответов, SQL-ограничений и чистоты текста.

Как проверить
-------------

Из папки Analytics:

  python3 -B -m unittest discover -s tests
  python3 -B tests/validate_project.py
  python3 -B -m analytics_assignment.report

Ожидаемый итог проверки:

  All project checks passed.

Примечание
----------

Проект не использует внешние зависимости. Для SQL-задания про покупки принято,
что операция покупки имеет type = 'BUY'. Если в базе используется другое кодовое
значение покупки, нужно заменить только этот литерал.
