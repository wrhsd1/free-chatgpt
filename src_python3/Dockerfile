FROM --platform=$TARGETPLATFORM python:3.7-alpine

COPY requirements.pip ./requirements.pip

RUN python3 -m pip install --upgrade pip

RUN pip install -U setuptools

RUN apk update

RUN apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev openssl-dev libffi-dev g++ && \
    python3 -m pip install -r requirements.pip --no-cache-dir && \
    apk --purge del .build-deps

RUN mkdir /work
WORKDIR /work

COPY . .

ENTRYPOINT ["python3", "main.py" ]
