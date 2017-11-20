FROM python:3-alpine

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY parameterstore-backup.py parameterstore-backup.py

ENTRYPOINT ["./parameterstore-backup.py"]
