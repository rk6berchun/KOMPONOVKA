import numpy as np
from Classes.Calc import Calculation


class SequentialAlgorithm:
    def __init__(self, input_data):
        self.data = input_data
        self.array_index = set(range(self.data.shape[0]))
        self.calculation = Calculation(self.data)
        self.n = list()
        self.subgraphs = list()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, input_data):
        assert isinstance(input_data, np.ndarray), "Invalid input data. Must be Numpy array"
        assert input_data.ndim == 2, "Invalid rang of matrix. Must be 2"
        assert input_data.shape[0] == input_data.shape[1], "Matrix must be quadratic"

        self.__data = input_data

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, input_n):
        assert sum(input_n) == self.data.shape[0] or not input_n, "Invalid number of vertexes. Must be sqrt(size of " \
                                                                  "matrix) "

        self.__n = input_n

    def start_seq(self, input_n):
        self.subgraphs = list()
        self.n = input_n
        array_index_temp = list(self.array_index)

        for group_size in self.n:
            if len(array_index_temp) != group_size:
                index = self.calculation.index_of_min_vdegree(array_index_temp)
                subgraph = self.calculation.create_subgraph(index, array_index_temp)

                while len(subgraph) < group_size:
                    subgraph = self.calculation.increase_subgraph(subgraph, array_index_temp)

                while len(subgraph) > group_size:
                    subgraph = self.calculation.optimize_subgraph(subgraph)

                self.subgraphs.append(subgraph)
                array_index_temp = list(self.array_index - set(item for row in self.subgraphs for item in row))
            else:
                self.subgraphs.append(array_index_temp)

        return self.subgraphs

    def start_iter(self):
        list_beta = list()
        vertexes = tuple()
        iterations = 0
        flag = True
        i = 0

        for cur_group in self.subgraphs[:-1]:
            for vertex_1 in cur_group:
                while vertexes or flag:
                    iterations += 1
                    flag = False
                    for other_group in self.subgraphs[i + 1:]:
                        for vertex_2 in other_group:
                            beta = self.calculation.beta_func(vertex_1, vertex_2, cur_group, other_group)
                            if beta > 0:
                                list_beta.append((vertex_1, vertex_2, cur_group, other_group, beta))
                    if list_beta:
                        args = sorted(list_beta, key=lambda x: x[-1])[-1][:-1]
                        self.calculation.swap(*args)
                        list_beta = list()
                flag = True

            i += 1
        # print(iterations)

    def objective_function(self):
        result = 0
        i = 0
        for cur_group in self.subgraphs[i:-1]:
            for vertex in cur_group:
                for other_group in self.subgraphs[i + 1:]:
                    result += self.data[vertex][other_group].sum()
            i += 1

        return result

    def __str__(self):
        return str.format("Куски для разрезания: {0} \n"
                          "Разбиение: {1} \n"
                          "Значение целевой функции: {2}", self.n, self.subgraphs, self.objective_function())
