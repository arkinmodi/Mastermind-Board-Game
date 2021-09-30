FROM python:3.9

WORKDIR /src

COPY src/ /src/

CMD [ "python3", "main.py" ]
