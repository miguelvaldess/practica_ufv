FROM tiangolo/uvicorn-gunicorn

RUN mkdir /fastapi

COPY requirements.txt /fastapi

WORKDIR /fastapi

RUN pip install -r requirements.txt

COPY . /fastapi

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8000"]
