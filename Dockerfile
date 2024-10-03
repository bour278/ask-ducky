FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "--worker-tmp-dir", "/dev/shm", "ask_ducky.wsgi"]