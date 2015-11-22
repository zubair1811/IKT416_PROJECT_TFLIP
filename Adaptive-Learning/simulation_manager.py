from Algorithms.Hobbit_Hood.hobbit_hood_base import hobbit_hood_base as hh_base
from Algorithms.Hobbit_Hood.hobbit_hood_sceptical import hobbit_hood_sceptical as hh_sceptical
import numpy as np



def get_expectation_matrix():
    # Create Hobbit Hood base instance
    base = hh_base()

    x = len(base.matrix)
    y = len(base.matrix[0])

    matrix = np.zeros(shape=(x, y))


    # Create history matrix aswell
    history_matrix = []
    for x in range(len(matrix)):
        row = []
        for y in range(len(matrix[x])):
            row.append([])
        history_matrix.append(row)



    return matrix, history_matrix


def assign_hobbit():
    return hh_sceptical()

