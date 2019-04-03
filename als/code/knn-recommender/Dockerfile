FROM ci-artifacts.devops.fds.com/emlp/emlp-python3.6

WORKDIR /srv/app/

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./src/main.py"]
