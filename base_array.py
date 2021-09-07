import numpy as np
from sklearn import model_selection

pileup_path = "/Users/ngc7293/kisohai/pickup_bases.txt"
np_path = "/Users/ngc7293/kisohai/pickup_bases.npy"

X = []
Y = []

with open(pileup_path, "r") as bases:

    line = bases.readline().rstrip("\r\n")

    bases_list = []

    while line:
        if line == "0|0":
            Y.append(0)
            line = bases.readline().rstrip("\r\n")
        elif line == ("1|0" or "0|1"):
            Y.append(1)
            line = bases.readline().rstrip("\r\n")
        elif line == "1|1":
            Y.append(2)
            line = bases.readline().rstrip("\r\n")
        elif line == ("2|0" or "0|2"):
            Y.append(1)
            line = bases.readline().rstrip("\r\n")

        elif line == "#":
            X.append(bases_list)
            bases_list = []
            line = bases.readline().rstrip("\r\n")

        else:
            li_bases_one_hot = []
            for i in line:
                if i == "A":
                    li_bases_one_hot.append([1, 0, 0, 0])
                elif i == "C":
                    li_bases_one_hot.append([0, 1, 0, 0])
                elif i == "G":
                    li_bases_one_hot.append([0, 0, 1, 0])
                elif i == "T":
                    li_bases_one_hot.append([0, 0, 0, 1])
                else:
                    li_bases_one_hot.append([0, 0, 0, 0])

            bases_list.append(li_bases_one_hot)
            line = bases.readline().rstrip("\r\n")

X = np.array(X)
Y = np.array(Y)

x_train, x_test, y_train, y_test = model_selection.train_test_split(X, Y)
xy = (x_train, x_test, y_train, y_test)

np.save(np_path, xy)
