FROM continuumio/anaconda3:2021.05
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD python server/server.py