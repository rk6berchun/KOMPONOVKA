import numpy as np


class Calculation:
    def __init__(self, input_matrix):
        self.matrix = input_matrix

    def index_of_min_vdegree(self, index_array):
        index = int()
        sum_ = 100
        for i in index_array:
            row_sum = self.matrix[i].sum()
            if row_sum < sum_:
                sum_ = row_sum
                index = i
        return index

    def create_subgraph(self, index, index_array):
        row = self.matrix[index]
        index_of_subgraph = [i for i in range(len(row)) if (i in index_array and row[i] != 0)]
        index_of_subgraph.append(index)

        return index_of_subgraph

    def delta_fun(self, vertex, index_of_subgraph):
        delta = self.matrix[vertex].sum() - 2 * self.matrix[vertex][index_of_subgraph].sum()

        return delta

    def optimize_subgraph(self, index_of_subgraph):
        vertex_to_del = np.array([self.delta_fun(i, index_of_subgraph) for i in index_of_subgraph]).argmax()
        index_of_subgraph.pop(vertex_to_del)

        return index_of_subgraph

    def increase_subgraph(self, index_of_subgraph, index_array):
        set_index_of_matrix = set(x for x in index_array)
        set_index_of_subgraph = set(item for item in index_of_subgraph)
        rest_of_matrix = list(set_index_of_matrix - set_index_of_subgraph)

        vertex = self.index_of_min_vdegree(rest_of_matrix)
        subgraph = self.create_subgraph(vertex, rest_of_matrix)
        index_of_subgraph += subgraph

        return index_of_subgraph

    def alpha_func(self, vertex, subgraph_1, subgraph_2):
        result = self.matrix[vertex][subgraph_2].sum() - self.matrix[vertex][subgraph_1].sum()
        if vertex in subgraph_2:
            result = - result

        return result

    def beta_func(self, vertex_1, vertex_2, subgraph_1, subgraph_2):
        alpha_1 = self.alpha_func(vertex_1, subgraph_1, subgraph_2)
        alpha_2 = self.alpha_func(vertex_2, subgraph_1, subgraph_2)
        r = self.matrix[vertex_1][vertex_2]
        beta = alpha_1 + alpha_2 - 2 * r

        return beta

    @staticmethod
    def swap(vertex_1, vertex_2, subgraph_1, subgraph_2):
        subgraph_1.remove(vertex_1)
        subgraph_1.append(vertex_2)
        subgraph_2.remove(vertex_2)
        subgraph_2.append(vertex_1)
