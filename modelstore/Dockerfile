FROM ci-artifacts.devops.fds.com/emlp/emlp-python3.6

WORKDIR /srv/app/

COPY . .

RUN pip install numpy && pip install pandas && pip install sklearn && pip install fuzzywuzzy[speedup] && pip install emlpfsms

RUN apt-get install unzip && mkdir data

ADD http://files.grouplens.org/datasets/movielens/ml-10m.zip ./data 

#ADD http://11.142.226.187:8000/ml-10m.zip /srv/app/data

RUN unzip data/ml-10m.zip -d ./data 

CMD ["python", "./src/main.py"]

