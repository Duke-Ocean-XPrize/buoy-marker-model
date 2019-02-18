import random
import numpy as np
input_arr = []

def remove_null(data):
    output = [x for x in data if x !='null']
    return output

def get_range(value, inputMin, inputMax, outputMin, outputMax):
    intputSpan = inputMax - inputMin
    outputSpan = outputMax - outputMin
    valueScaled = float(value - inputMin) / float(intputSpan)
    return outputMin + (valueScaled * outputSpan)

def get_window(data, n):
    tranformed_data = get_range(data, 1, 30, 100, 1000)
    input_arr.append(tranformed_data)
    if len(input_arr) > n:
        del input_arr[0]
    return input_arr

def weighted_sum(data):
    """
    do something like this with future error weights 
    weighted_avg = np.average(sorted_window, weights=amount_err)
    """
    window = get_window(data, 4)
    sorted_window = sorted(window, reverse = True)
    av = sum(sorted_window[3:])/3
    return av



while True:
    input_data = random.randint(1, 30)
    print(weighted_sum(input_data))

