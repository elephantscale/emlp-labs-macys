# Jupyter Notebok on EMLP

This is setting up juptyer notebook on EMLP

## Step 1: Create a New Pipeline
![](../images/jupyter-1-createnew.png)

## Step 2: Give the Pipeline a Name
![](../images/jupyter-2-pipelinename.png)

## Step 3: Give the Pipeline a Definition
![](../images/jupyter-3-pipeline-def.png)

## Step 3: Launch the Jupyter notebook
![](../images/jupyter-4-pipeline-launch.png)

## Step 4: Open a Notebook
![](../images/jupyter-5-launch-notebook.png)

## Step 5: install tensorflow with pip

Install tensorflow like this:

```pycon
!sudo pip install tensorflow
```

![](../images/jupyter-6-pip-install.png)


## Step 6: Do a hello world code with tensorflow

```python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
```

![](../images/jupyter-7-hello-tensorflow.png)


