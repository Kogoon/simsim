FROM python:3.9.12-slim

RUN pip install flask flask_bootstrap

COPY ./ /
WORKDIR /

#RUN python db.py

CMD ["python", "main.py"]
