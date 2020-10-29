FROM python:3.6

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install .

ENTRYPOINT ["python"]

EXPOSE 8000

CMD ["__init__.py"]
