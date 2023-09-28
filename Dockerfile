FROM bitnami/python:3.10.5

RUN pip install --upgrade pip

WORKDIR /nightwatch

COPY ./requirements.txt /nightwatch/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /nightwatch/requirements.txt

COPY ./app /nightwatch/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]