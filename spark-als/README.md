# Spark ALS

Here we are going to do a spark ALS example


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

Call it `YOURNAME-spark-als`

Go ahead and save.


## Go to tasks

Go to create a task.

Create task by the name of "pyspark-task"

Use the starter template `Python3-Pyspark2.4-Spark2.4-bq`

![](../images/wordcount-1-task.png)



## Create a step for your task

Create a step for your task.



## Go to Gitlab

It should be at the following address [Gitlab](https://code.devops.fds.com/)

```text
https://code.devops.fds.com/
```


## Clone the repo

Go ahead and clone your repo.

## Copy the file and c ommit and push

copy the file `src/main.py` to the repo.
copy the data files `src/*.csv` to the repo

Make changes to the main.py file by copying [this file](./src/main.py)

Also go ahead and add the data which is [src/ratings.csv](./src/ratings.csv) and [src/movies.csv](./src/movies.csv)


```bash

git add src/*.csv
git add src/main.py
git commit -m "Added source and data file"
git push
```

## Edit the requirements.txt file in the repo

You will need to add the following:

```text
numpy
pandas
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

16 latent factors and regularization = 0.2: validation RMSE is 0.0
18 latent factors and regularization = 0.001: validation RMSE is 0.0
18 latent factors and regularization = 0.01: validation RMSE is 0.0
18 latent factors and regularization = 0.05: validation RMSE is 0.0
18 latent factors and regularization = 0.1: validation RMSE is 0.0
18 latent factors and regularization = 0.2: validation RMSE is 0.0
20 latent factors and regularization = 0.001: validation RMSE is 0.0
20 latent factors and regularization = 0.01: validation RMSE is 0.0
20 latent factors and regularization = 0.05: validation RMSE is 0.0
20 latent factors and regularization = 0.1: validation RMSE is 0.0
20 latent factors and regularization = 0.2: validation RMSE is 0.0
The best model has 8 latent factors and regularization = 0.001
Total Runtime: 359.70 seconds
The out-of-sample RMSE of rating predictions is 0.0
Recommendations for Batman:
1: Tashunga (1995)
2: Senseless (1998)
3: Just the Ticket (1999)
4: Towering Inferno, The (1974)
5: Empty Mirror, The (1996)
6: Ghostbusters (a.k.a. Ghost Busters) (1984)
7: Dersu Uzala (1975)
8: Cherry 2000 (1987)
9: Nico and Dani (Krámpack) (2000)
========================================>   (13 + 1) / 14]

```


