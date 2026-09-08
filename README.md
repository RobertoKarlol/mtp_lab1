# Лабораторная работа №1. Система контроля версий

[![Python code check](https://github.com/RobertoKarlol/mtp_lab1/actions/workflows/python-check.yml/badge.svg)](https://github.com/RobertoKarlol/mtp_lab1/actions/workflows/python-check.yml)

<!-- ЗАПОЛНИТЕ СТРОКУ НИЖЕ: ФИО полностью и номер группы -->
**ФАМИЛИЯ ИМЯ ОТЧЕСТВО, группа ГГГГГГ-ГГ, вариант 5, лабораторная №1**

Дисциплина: «Методы и технологии программирования» (часть 1).

## Задания варианта 5

Номера заданий взяты из общего списка методички (строка «5» таблицы
индивидуальных вариантов: `5 7 1 6 8`).

| Категория | № в списке | Формулировка | Где смотреть результат |
|---|---|---|---|
| Средняя 1 | 5 | Создать ветку `feature`, добавить новый файл | ветка `feature`, каталог `lab1/`, merge-коммит |
| Средняя 2 | 7 | Создать файл `.gitignore` для Python | `.gitignore` |
| Средняя 3 | 1 | Установить Git и настроить имя, email | `docs/lab1/01-git-setup.md` |
| Повышенная 1 | 6 | Настроить GitHub Actions для проверки Python-кода | `.github/workflows/python-check.yml` |
| Повышенная 2 | 8 | Использовать git submodules | `.gitmodules`, `external/six` |

Отчёт и команды для проверки: [`docs/lab1/report.md`](docs/lab1/report.md).

## Структура добавленного

```
.github/workflows/python-check.yml  # CI: flake8 + unittest (повышенная 1)
.gitignore                          # правила игнорирования Python (средняя 2)
docs/lab1/01-git-setup.md           # установка и настройка Git (средняя 3)
docs/lab1/report.md                 # отчёт по лабораторной работе
external/six                        # подмодуль (повышенная 2)
lab1/repo_info.py                   # файл, добавленный в ветке feature (средняя 1)
lab1/tests/test_repo_info.py        # модульные тесты, их запускает CI
```

## Как проверить работу локально

```bash
git clone --recurse-submodules https://github.com/RobertoKarlol/mtp_lab1.git
cd mtp_lab1
python -m pip install flake8==5.0.4 flake8-docstrings==1.7.0 pep8-naming==0.13.3
flake8 .
python -m unittest discover -s lab1/tests -t .
python -m lab1.repo_info
```
