# Отчёт по лабораторной работе №1

**Студент:** Нгуен Роберт Ламович, группа 221341.
**Тема:** система контроля версий Git.
**Вариант:** 5.

По таблице вариантов выполнены задания средней сложности №5, №7, №1
и повышенной сложности №6, №8.

## 1. Установка и настройка Git

Для проверки установки и настройки автора используются команды:

```bash
git --version
git config --local user.name "RobertoKarlol"
git config --local user.email "joppoj8@gmail.com"
git config --local --get user.name
git config --local --get user.email
```

Параметры `user.name` и `user.email` задают сведения об авторе коммитов.
Ключ `--local` ограничивает настройку текущим репозиторием.
Подробнее: [настройка Git](01-git-setup.md).

## 2. Игнорирование файлов Python

В `.gitignore` указаны байт-код Python, виртуальные окружения, кеши
проверок, файлы редактора и локальные переменные окружения.

Проверить основные правила можно без создания файлов:

```bash
git check-ignore -v lab1/__pycache__/example.pyc example.pyc .env .env.local
```

## 3. Ветка feature и новый файл

В ветке `feature` добавлен `lab1/repo_info.py`. Скрипт вызывает Git
и выводит текущую ветку, число коммитов и их распределение по авторам.
Разбор вывода Git и форматирование результата проверяются пятью тестами.

```bash
python -m lab1.repo_info
python -m unittest discover -s lab1/tests -t .
```

Ветка `feature` сохранена на GitHub. Её изменения вошли в рабочую ветку
через отдельный merge-коммит, затем были включены в `main`.
Посмотреть добавление файла и слияния:

```bash
git log --all --diff-filter=A -- lab1/repo_info.py
git log --graph --oneline --all
git shortlog -s -n --all
```

Число коммитов зависит от состояния репозитория на момент проверки.

## 4. GitHub Actions

Файл `.github/workflows/python-check.yml` задаёт проверку на Ubuntu
с Python 3.11. Проверка запускается при push, pull request и вручную.

Последовательно выполняются:

```bash
flake8 .
python -m compileall -q lab1
python -m unittest discover -s lab1/tests -t .
```

Результаты запусков доступны во вкладке
[Actions](https://github.com/RobertoKarlol/mtp_lab1/actions).

## 5. Подмодуль

Библиотека `six` подключена как Git-подмодуль в `external/six`.
Она нужна для демонстрации работы с подмодулями; скрипт статистики
репозитория её не импортирует.

Подмодуль закреплён на версии `1.16.0`, коммит
`65486e4383f9f411da95937451205d3c7b61b9e1`.
Адрес и путь записаны в `.gitmodules`, а коммит — в дереве Git.

```bash
git submodule update --init --recursive
git submodule status
git ls-tree HEAD external/six
```

Для клонирования вместе с подмодулем:

```bash
git clone --recurse-submodules https://github.com/RobertoKarlol/mtp_lab1.git
```

## Результат

Создана ветка с новым Python-модулем, настроено игнорирование локальных
файлов, указаны сведения об авторе коммитов. На GitHub настроены
автоматические проверки и подключён подмодуль с фиксированной версией.
