FROM python:3.7

COPY . /api

WORKDIR /api

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["run.py"]
