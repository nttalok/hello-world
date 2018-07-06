FROM python:2.7-slim

WORKDIR /devops/demo/data/introapp
ADD . /devops/demo/data/introapp
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME "NTT Data Cloud Team"
CMD ["python","app.py"]
