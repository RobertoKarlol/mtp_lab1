"""Сбор сведений о Git-репозитории проекта.

Модуль добавлен в ветке ``feature`` в рамках задания «Средняя 1»
(№5 общего списка) лабораторной работы №1.
"""

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def run_git(*args):
    """Вернуть вывод git-команды, выполненной в корне репозитория."""
    completed = subprocess.run(
        ('git', *args),
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return completed.stdout.strip()


def parse_shortlog(text):
    """Разобрать вывод ``git shortlog -s -n`` в список пар.

    Пара состоит из имени автора и количества его коммитов.
    Пустые строки пропускаются.
    """
    authors = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        count, _, name = line.partition('\t')
        if not name:
            count, _, name = line.partition(' ')
        authors.append((name.strip(), int(count)))
    return authors


def format_summary(branch, commits, authors):
    """Собрать текстовую сводку по репозиторию."""
    lines = [
        f'Текущая ветка: {branch}',
        f'Всего коммитов: {commits}',
        'Авторы:',
    ]
    lines.extend(f'  {name}: {count}' for name, count in authors)
    return '\n'.join(lines)


def collect_summary():
    """Собрать сводку, обращаясь к настоящему репозиторию."""
    branch = run_git('rev-parse', '--abbrev-ref', 'HEAD')
    commits = int(run_git('rev-list', '--count', 'HEAD'))
    authors = parse_shortlog(run_git('shortlog', '-s', '-n', 'HEAD'))
    return format_summary(branch, commits, authors)


def main():
    """Напечатать сводку по репозиторию."""
    print(collect_summary())


if __name__ == '__main__':
    main()
