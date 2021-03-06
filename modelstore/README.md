# ModelStore

Here we are going to do a modelstore example


## clone this repo on your computer

```console
cd
git clone https://github.com/elephantscale/emlp-labs-macys.git 
```

## Set your name in your bash shell

Open up a bash shell.

```bash
export YOURNAME=<enter your name here>
```

This environment variable will make life easier. Remember this name that you used


## Go to EMLP Staging in your browser

Go to [EMLP dev](http://dev.emlp.macysdev.net/emlp)

```text
http://dev.emlp.macysdev.net/emlp
```

## Click on Add New

![](../images/als-2-addnew.png)

## Create the name

Call it `YOURNAME-modelstore`

Go ahead and save.


## Go to tasks

Go to create a task.

Create task by the name of "t1"

Use the starter template `Python3-Pyspark2.4-Spark2.4-bq`

![](../images/wordcount-1-task.png)


## Add an environment variable

![](../images/modelstore-1.png)

## Add Secrets Volume

![](../images/modelstore-2.png)


## Create a step for your task

Create a step for your task.



## Go to Gitlab

It should be at the following address [Gitlab](https://code.devops.fds.com/)

```text
https://code.devops.fds.com/
```


## Clone the repo

Go ahead and clone your repo.

## Copy the files and commit and push

copy the file `src/main.py` to the repo.

Make changes to the main.py file by copying [this file](./src/main.py)

copy the Dockerfile



```bash

git add src/main.py
git add Dockerfile
git commit -m "Added source and data file"
git push
```



## Run the Workflow

![](../images/helloworld7-run.png)

## List Running
![](../images/helloworld8-listrunning.png)

## Start Apache Argo
![](../images/wordcount-2-argo.png)

## Look at Logs

![](../images/helloworld10-logs.png)

You should see something like this;

```text

```


