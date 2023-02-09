FROM python:3.10

ENV USES_DOCKER Yes

## Falta desarrollar la base de datos

WORKDIR /fastapi-five-stars-car-service
COPY requirements.txt /fastapi-five-stars-car-service/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /fastapi-five-stars-car-service/requirements.txt

COPY . /fastapi-five-stars-car-service/

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]