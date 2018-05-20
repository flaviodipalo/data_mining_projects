import keras.layers as klayers
import keras as k
import models.keras.custom_activations as acts


def simpleNN(num):
    input = klayers.Input(shape=(num,))
    x = klayers.Dense(units=300, activation='linear', use_bias=True)(input)
    x = klayers.Dense(units=1, activation='relu')(x)
    return k.Model(inputs=input, outputs=x)


def nonsequentialNN(num, last_relu=True):
    inputs = klayers.Input(shape=(num,))

    y = klayers.Dense(units=500, activation='tanh', use_bias=True)(inputs)
    x = klayers.Dense(units=500, activation='relu', use_bias=True)(inputs)
    z = klayers.Dense(units=500, activation='sigmoid', use_bias=True)(inputs)
    x = klayers.concatenate([klayers.multiply([x, y]), z])

    x = klayers.Dense(units=500, activation='relu', use_bias=True)(x)
    x = klayers.Dense(units=500, activation='relu', use_bias=True)(x)
    if last_relu:
        x = klayers.Dense(units=1, activation='relu', use_bias=True)(x)
    else:
        x = klayers.Dense(units=1, activation='linear', use_bias=True)(x)
    return k.Model(inputs=inputs, outputs=x)
