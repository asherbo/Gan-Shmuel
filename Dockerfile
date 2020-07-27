FROM python:latest
COPY app /app
WORKDIR /app

RUN pip freeze > requirements.txt
# RUN pip install -r requirements.txt
# RUN ls -1
# RUN pwd
# ENTRYPOINT [ "" ]

