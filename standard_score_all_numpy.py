import numpy as np

data = []
while True:
    input_text = input()
    if input_text == "break":
        break
    else:
        input_text = int(input_text)
        data.append(input_text)
mean_value_of_data = np.mean(data)
std = np.std(data)
length_of_data = len(data)

for i in range(length_of_data):
    out = data[i]
    ss = (((out - mean_value_of_data) / std) * 10) + 50
    print(f"{i + 1}人目の偏差値は、{ss}です。")