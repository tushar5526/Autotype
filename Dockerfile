FROM ubuntu

RUN apt update 

RUN apt-get install -y \
    wget \
    libcanberra-gtk-module \
    libcanberra-gtk3-module


RUN cd /tmp && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb

RUN apt install vim -y
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /opt/autotype

COPY . /opt/autotype/

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["google-chrome", "--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]


