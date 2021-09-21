FROM python:3.8.2

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /opt/yijunx/code

COPY './requirements.txt' .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "app.app:app", "-w", "3", "-b", "0.0.0.0:8000"]