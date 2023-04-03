import numpy as np

data = []
list2 = []
while True:
    input_text = input()
    if input_text == "break":
        break
    else:
        input_text = int(input_text)
        data.append(input_text)
mean_value_of_data = np.mean(data)
length_of_data = len(data)

def std(data):
    average = sum(data) / len(data)
    dispersion = sum([(value - average) ** 2 for value in data]) / len(data)
    return np.sqrt(dispersion)

std1 = std(data)

for i in range(length_of_data):
    out = data[i]
    ss = ((out - mean_value_of_data) / float(std1)) * 10 + 50 
    print(f"{i + 1}人目の偏差値は、{ss}です。")