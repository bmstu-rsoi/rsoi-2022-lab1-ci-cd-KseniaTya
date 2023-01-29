FROM python:latest
COPY . /app
WORKDIR /app
EXPOSE 3000
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD ["sh", "-c", "python3 app.py runserver 0.0.0.0:$PORT" ]

