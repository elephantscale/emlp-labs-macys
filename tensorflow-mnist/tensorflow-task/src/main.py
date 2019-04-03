import logging
import tensorflow as tf

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)


def return_something(some_string: str) -> str:
    """

    :param some_string: some string to return
    :return: A string
    """
    LOG.info('Returning %s', some_string)
    return some_string



if __name__ == '__main__':
    mnist = tf.keras.datasets.mnist

    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=1)
    model.evaluate(x_test, y_test)
    LOG.info('DONE!')
