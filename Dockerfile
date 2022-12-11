FROM python:3.10.5

WORKDIR /app/

COPY . .

RUN apt-get update && apt-get upgrade -y

RUN apt-get install git curl sudo wget jq python3-pip ffmpeg -y 

RUN pip3 install --upgrade pip setuptools

RUN pip install -U -r requirements.txt

CMD ["python3","-m","PokeTide"]
