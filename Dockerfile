FROM python:latest
WORKDIR /app
RUN  pip install flask
ENTRYPOINT [ "python", "app.py" ] 



# RUN pip freeze > requirements.txt
# RUN pip install -r requirements.txt
