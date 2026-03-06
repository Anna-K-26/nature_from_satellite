import dill
import matplotlib.pyplot as plt
import numpy as np

with open('dataset_t5r10_ts0.1.bin', 'rb') as dump:
    X_train, X_test, y_train, y_test = dill.load(dump)

print("x_train = {}".format(X_train[:, 9:10]))
print("x_test = {}".format(X_train[:, 9:10]))
print(y_train.shape[1])
print(y_test.shape[1])

plt.figure(figsize=(10, 5))

# matrix = []
f0 = np.round(np.arange(18., 40.1, 0.2), decimals=1)
f1 = np.round(np.arange(50., 55.1, 0.2), decimals=1)
f2 = np.round(np.arange(65., 70.1, 0.2), decimals=1)
f3 = np.round(np.arange(183.3 - 5, 183.3 + 5.1, 0.2), decimals=1)
frequencies = np.hstack((f0, f1, f2, f3))

T = X_train[0, 7:]

if len(T) >= len(frequencies):
    T_new = T[:len(frequencies)]
    frequencies_new = frequencies
else:
    T_new = T[:]
    frequencies_new = frequencies[:len(T)]
# for elem in frequencies:
#     if 40 < elem < 50 or 55 < elem < 65 or 70 < elem < 183.3 - 5:
#         matrix.append(None)
#     else:
#         matrix.append(elem)
# matrix_array = np.array(matrix, dtype=object)
# print(matrix_array)
plt.scatter(frequencies_new, T_new, color='blue', s=30)
plt.yscale('log')
plt.xlabel('f')
plt.ylabel('lgT')
plt.show()






