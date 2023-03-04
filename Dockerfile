FROM python:3.10.6-slim
COPY . /home
WORKDIR /home
COPY . .
RUN pip install --upgrade pip
RUN pip install Flask gunicorn

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app