
FROM python:3.7.0a4

WORKDIR /Users/user/desktop/project/test

ADD . /Users/user/desktop/project/test

RUN pip install -r requirements.txt

EXPOSE 8080

ENV NAME World

 CMD ["python", "hello_world.py"]