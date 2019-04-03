# Spark ALS


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

Go to [EMLP Staging](http://stage.emlp.macysdev.net/emlp)

```text
http://stage.emlp.macysdev.net/emlp
```


![](../images/als-1-emlp.png)

## Click on Add New and create name

![](../images/mnist-1-create-pipeline.png)



![](../images/als-3-name.png)

## Create the workflow

![](../images/als-4-create.png)

## Go to tasks

![](../images/mnist-2-create-task.png)

![](../images/als-7-createtask1.png)

## Create a task

![](../images/mnist-3-create-task-name.png)

*  tensorflow-task

Use "Python3" 


Here we will be using a custom set of resources
![](../images/mnist-4-create-task-resources.png)

Create a task 

Just accept the defaults for the command and again click next.

We don't need any environment variables so again click next.

We don't need a volume so at the very end click "Create"

Repeat the same for als-recommender.

![](../images/als-8-taskname.png)

## Create 2 Steps

Go to steps:
![](../images/mnist-5-create-step.png)


Create 2 Steps:

1. `running-als`
2. `running-knn`

Just accept defaults for both

![](../images/mnist-6-add-step.png)

Here is what is should look like when you create the stps:

![](../images/mnist-7-step-done.png)





## Go to Gitlab

It should be at the following address [Gitlab](https://code.devops.fds.com/emlp-stage)

```text
https://code.devops.fds.com/emlp-stage
```
![](../images/mnist-8-gitlab.png)

## Find your repo by name 

You can use the filter option.


## Copy the repo name

Copy that to your clipboard



## Clone the repo

```bash
cd
git clone git@code.devops.fds.com:emlp-stage/$YOURNAME-tensorflow-mnist.git
```




## Copy the files to the repository

```console
cp ~/emlp-labs-macys/tensorflow-mnist/tensorflow-task/requirements.txt ~/$YOURNAME-tensorflow-mnist/tensorflow-task/
cp ~/emlp-labs-macys/tensorflow-mnist/tensorflow-task/src/main.py ~/$YOURNAME-tensorflow-mnist/tensorflow-task/src/

```
## Add the files to your gitlab repository

```console
cd ~/$YOURNAME-tensorflow-mnist
git add tensorflow-task/requirements.txt
git add tensorflow-task/src/main.py
```

## Check git status and make sure it looks right

```console
git status
```


## Check your email and make sure it says your Macy's email and not something else

```
git config --user.email
```

## Now do a commit and push

```
git commit
# Enter your commit message
git push
```

## Check jenkins to make sure it is there.


```text
https://platform-ci.devops.fds.com/jenkins/view/EMLP/view/Jobs/job/emlp-build/
```

Wait until the job is finished building


## Run the Workflow

![](../images/helloworld7-run.png)

## List Running
![](../images/helloworld8-listrunning.png)

## Start Apache Argo
![](../images/helloworld9-argo.png)

## Look at Logs

![](../images/helloworld10-logs.png)




