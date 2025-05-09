FROM python
RUN apt-get update && apt-get install python3-pip -y
WORKDIR /projeto
COPY . /projeto/
COPY ./requirements.txt /projeto
COPY ./app /projeto
COPY ./app/main.py /projeto
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port", "5000"] 