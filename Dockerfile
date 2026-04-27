FROM python:slim

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
