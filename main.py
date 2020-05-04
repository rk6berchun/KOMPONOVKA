from Classes.SeqAlgorithm import SequentialAlgorithm
import os
import csv
import numpy as np


N = ([3, 6, 7, 7, 7], [4, 5, 7, 7, 7], [4, 6, 6, 7, 7], [5, 5, 6, 7, 7], [5, 6, 6, 6, 7], [6, 6, 6, 6, 6],
     [3, 3, 3, 7, 7, 7], [3, 3, 4, 6, 7, 7], [3, 3, 5, 5, 7, 7], [3, 3, 5, 6, 6, 7], [3, 3, 6, 6, 6, 6],
     [3, 4, 4, 5, 7, 7], [3, 4, 4, 6, 6, 7], [3, 4, 5, 5, 6, 7], [3, 4, 5, 6, 6, 6], [3, 5, 5, 5, 5, 7],
     [3, 5, 5, 5, 6, 6], [4, 4, 4, 4, 7, 7], [4, 4, 4, 5, 6, 7], [4, 4, 4, 6, 6, 6], [4, 4, 5, 5, 5, 7],
     [4, 4, 5, 5, 6, 6], [4, 5, 5, 5, 5, 6], [5, 5, 5, 5, 5, 5], [3, 3, 3, 3, 4, 7, 7], [3, 3, 3, 3, 5, 6, 7],
     [3, 3, 3, 3, 6, 6, 6], [3, 3, 3, 4, 4, 6, 7], [3, 3, 3, 4, 5, 5, 7], [3, 3, 3, 4, 5, 6, 6], [3, 3, 3, 5, 5, 5, 6],
     [3, 3, 4, 4, 4, 5, 7], [3, 3, 4, 4, 4, 6, 6], [3, 3, 4, 4, 5, 5, 6], [3, 3, 4, 5, 5, 5, 5], [3, 4, 4, 4, 4, 4, 7],
     [3, 4, 4, 4, 4, 5, 6], [3, 4, 4, 4, 5, 5, 5], [4, 4, 4, 4, 4, 4, 6], [4, 4, 4, 4, 4, 5, 5],
     [3, 3, 3, 3, 3, 3, 5, 7], [3, 3, 3, 3, 3, 3, 6, 6], [3, 3, 3, 3, 3, 4, 4, 7], [3, 3, 3, 3, 3, 4, 5, 6],
     [3, 3, 3, 3, 3, 5, 5, 5], [3, 3, 3, 3, 4, 4, 4, 6], [3, 3, 3, 3, 4, 4, 5, 5], [3, 3, 3, 4, 4, 4, 4, 5],
     [3, 3, 4, 4, 4, 4, 4, 4], [3, 3, 3, 3, 3, 3, 3, 3, 6], [3, 3, 3, 3, 3, 3, 3, 4, 5], [3, 3, 3, 3, 3, 3, 4, 4, 4],
     [3, 3, 3, 3, 3, 3, 3, 3, 3, 3])

filename = "Data.csv"
folder = os.path.join(os.getcwd(), "InputData")
path = os.path.abspath(os.path.join(folder, filename))
print(path)
assert os.path.exists(path), "Incorrect name of file or path"
temp_list = list()
with open(path, "r") as f_obj:
    reader = csv.reader(f_obj)
    for row in reader:
        temp_list.append([int(x) for x in row])


seq_alg = SequentialAlgorithm(np.array(temp_list))

for input_group in N:
    seq_alg.start_seq(input_group)
    print("Последовательный алгоритм")
    print(seq_alg)
    print("Итерационный алгоритм")
    seq_alg.start_iter()
    print(seq_alg, "\n")
