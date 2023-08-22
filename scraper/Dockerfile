FROM python:3.10-alpine

RUN adduser -D user
ADD requirements.txt .

RUN apk add build-base postgresql-dev
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /app
ENV PYTHONPATH=/app
USER user

ADD . /app

CMD ["sh", "start.sh"]
