# Проект парсинга версий языка Python и PEP.

### Описание

Проект Парсера который через данные из cmd собирает данные с сайтов и в зависимости от команды выводит эти данные либо непосредственно в терминал, либо в отдельный файл.

В проекте встроено логирование.

## Stack

Python 3.8, beautifulsoup4 4.9.3, requests 2.27.1

### Установка, Как запустить проект:
https://github.com/Alex386386/bs4_parser_pep
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Alex386386/bs4_parser_pep
```

```
cd bs4_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Все дальнейшие инструкции по использованию приложения вы можете найти сделав следующее:

```
cd src
```

Введите команду:

```
python main.py -h
```

Автор:
- [Александр Мамонов](https://github.com/Alex386386) 