# Отзывы с двумя ручками
Приложение имеет два endpoint, анализирует настроение отзыва по простому наличию в тексте отзыва положительных или отрицательных слов.
####
Пример, отзыва: "Люблю этот товар" — слово "люблю" => positive
~~~url
POST /reviews
Schema {"text": "string"}
~~~
и
~~~url
GET /reviews&sentiment=***
*** Any From (positive, negative, neutral)
~~~

### Установка и Запуск (Windows & Linux)
#### Linux
Перейдите в директорию проектов и выполните клонирование
~~~bash
git clone https://github.com/ImOneDollarBun/SentimentReview.git
cd SentimentReview
~~~
Установите зависимости и запустите приложение
Убедитесь, что у вас есть пакет python с виртуальным окружением
~~~bash
apt install python3.8-venv
~~~
~~~bash
python -m venv venv
source venv/bin/activate
~~~
~~~bash
pip install -r requirements.txt
~~~
~~~bash
python main.py
~~~
Можно запустить при помощи uvicorn указав хост, порт, и параметры
~~~bash
uvicorn main:app
~~~
~~~bash
uvicorn main:app --host 127.0.0.1 --port 12345
~~~
#### Windows
Распакуйте скачанных архив или клонируйте репозиторий
~~~bash
git clone https://github.com/ImOneDollarBun/SentimentReview.git
cd SentimentReview
~~~
Активируйте виртуальное окружение pip и установите зависимости
~~~bash
python -m venv venv
source venv/bin/activate
~~~
~~~bash
pip install -r requirements.txt
~~~
Запуск
~~~bash
python main.py
~~~

### Примеры использования
Запрос на отправку отзыва с текстом "люблю"
~~~bash
curl -X 'POST' \
  'http://127.0.0.1:8000/reviews' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "люблю"
}'
~~~
Запрос на получение всех положительных отзывов
~~~bash
curl -X 'GET' \
  'http://127.0.0.1:8000/reviews?sentiment=positive' \
  -H 'accept: application/json'
~~~
~~~text
[
  [
    1,
    "люблю",
    "positive",
    "2025-07-28T08:35:49.197259"
  ]
]
~~~