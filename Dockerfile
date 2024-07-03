FROM python:3 AS builder

WORKDIR /code

LABEL author="hesamdavarpanah"

COPY requirements.txt . 

FROM python:3-alpine

WORKDIR /code

RUN apk update 
RUN apk upgrade --no-cache
RUN apk add --no-cache netcat-openbsd net-tools iputils-ping zsh curl wget nano git

RUN apk del

COPY --from=builder /code/requirements.txt .

RUN pip install --no-cache-dir --timeout=300 --upgrade -r /code/requirements.txt

COPY . /code

RUN chmod +x ./run.sh

RUN chmod -R 777 ./

CMD ["./run.sh"]