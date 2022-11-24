FROM python


COPY requirements.txt /app/requirements.txt


WORKDIR /app


RUN pip3 install --no-cache-dir -r requirements.txt


RUN apt-get update -y


RUN apt-get install tk -y


COPY . /app


CMD ["python3","GUI_script.py"]