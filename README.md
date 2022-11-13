# From_OpenVino_to_neo4j_converter

Этот инструмент позволяет конвертировать файлы моделей нейронных сетей OpenVino в базу данных neo4j.

# Скачайте репозиторий

    clone https://github.com/s3m3n1s/From_OpenVino_to_neo4j_converter.git
    cd From_OpenVino_to_neo4j_converter

# Запуск

## Запуск базы данных

Запустите базу данных neo4j:

    docker-compose up -d


## Установка зависимостей 

Установите парсер и драйвер neo4j:

    pip3 install -r requirements.txt
   или

    sudo pip3 install -r requirements.txt

## Запуск конвертера

    python3 main.py

## Укажите xml файл модели

Модель нейронной сети в формате OpenVino состоит из .bin файла с весами и .xml файла со структурой нейронной сети.
Для построения графа нам потребуется только .xml файл
Их можно скачать по ссылкам из репозитория:
[репозиторий моделей OpenVino](https://github.com/openvinotoolkit/open_model_zoo)
2 файла оттуда уже есть в репозитории, можно протестировать запуск на них:

`emotions-recognition-retail-0003.xml` и `resnet50-binary-0001.xml`
Введите одно из этих имён в программу.

# Просмотр графа
Откройте браузер и перейдите по ссылке:

    http://localhost:7474/browser/
Введите имя пользователя и пароль:

    neo4j:neo4j

В появившейся строке ввода команд введите:

    match (n) return (n)
Возможно появление предупреждения:

    Not all return nodes are being displayed due to Initial Node Display setting. Only first 300 nodes are displayed.
Тогда стоит увеличить количество отображаемых нод в настройках 
.
