FROM python:3.8

COPY mc_bot /app
WORKDIR /app

RUN pip3 install -U setuptools
RUN apt-get install -y libssl-dev libffi-dev 
RUN apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev 
RUN pip3 install -r requirements.txt

CMD ["python3","bot.py"]
