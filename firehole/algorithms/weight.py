# -*- coding: utf-8 -*-
"""
==========================
Evaluate and score systems
==========================
"""
import numpy as np
from firehole.exception import FireHoleNotArray
__author__ = '''Xia Tian (xsumner@hotmail.com)'''


class Entropy:
    def __init__(self):
        print("Welcome to use FireHole, this is Entropy Method !\n")
        print("For more usage, please refer to the examples folder.")

    @staticmethod
    def matrix_standardization(matrix):
        # standardize the input matrix (max-min standardization)
        standard_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())
        return standard_matrix

    @staticmethod
    def get_entropy(matrix):
        # get the column number and row number
        m, n = matrix.shape
        k = 1 / np.log(m)
        # Add by column (axis=0: add by columns; axis=1: add by rows)
        yij = matrix.sum(axis=0)
        # pij is the prior probability of yij
        pij = matrix / yij
        # use seterr to avoid warning(for temporary)
        np.seterr(divide='ignore', invalid='ignore')
        test = pij * np.log(pij)
        np.seterr(divide='warn', invalid='warn')
        # Replace nan with 0
        test = np.nan_to_num(test)
        # Calculate the entropy of each column
        ej = -k * (test.sum(axis=0))
        # Calculate the weights
        wi = (1 - ej) / (n - np.sum(ej))

        return ej, wi

    @staticmethod
    def get_score(data_matrix, weight_matrix):
        weight_matrix = weight_matrix.copy()
        data_matrix = data_matrix.copy()
        # Calculate the final scores
        scores = weight_matrix * data_matrix
        return scores.sum(axis=0)

    def entropy(self, data):
        """Return a result dict of entropy method

        Raise an exception if the input is not numpy array

        Parameters
        ----------
        data : numpy array

        Returns
        -------
        entropy_rlt : dictionary
            A dictionary with keys of 3 strings and value of 3 numpy array

        Examples
        --------
        """
        data = data.copy()
        data_type = type(data)
        if data_type != np.ndarray:
            raise FireHoleNotArray('data', data_type)
        standard_matrix = self.matrix_standardization(data)
        entropy_value, weight = self.get_entropy(standard_matrix)
        score = self.get_score(standard_matrix, weight)
        entropy_rlt = {"entropy": entropy_value, "weight": weight, "score": score}
        return entropy_rlt


class COV:
    def __init__(self):
        print("Welcome to use FireHole, this is coefficient of variation method !\n")
        print("For more usage, please refer to the examples folder. ")

    @staticmethod
    def coefficient_of_variation(data):
        data_type = type(data)
        if data_type != np.ndarray:
            raise FireHoleNotArray('data', data_type)
        # standard deviation divided by mean (without nan value)
        v = np.nanstd(data, axis=0) / np.nanmean(data, axis=0)
        return v

    def comprehensive(self, data, target, pos_neg=1, decimals=4):
        """Return a result dict of coefficient  method

        Raise an exception if the input is not numpy array

        Parameters
        ----------
        data : numpy array
        target : numpy array
        pos_neg : numpy array
        decimals: int

        Returns
        -------
        cov_rlt : numpy array
            A numpy array of the final score

        Examples
        ----
        """
        # check the target data type
        target_type = type(target)
        if target_type != np.ndarray:
            raise FireHoleNotArray('target', target_type)
        # check the input size to avoid Broadcasting Error !
        data_shape = set(data.shape)
        target_shape = set(target.shape)
        shape_set = data_shape & target_shape
        if shape_set == set():
            raise Exception("data and target should have at least one same size !")
        if [pos_neg != 1]:
            pos_neg_type = type(pos_neg)
            if pos_neg_type != np.ndarray:
                raise FireHoleNotArray('pos_neg', pos_neg_type)
            pos_neg_shape = set(pos_neg.shape)
            if pos_neg_shape & shape_set == set():
                raise Exception("pos_neg has wrong size !")
        # calculate the coefficient of variation
        v = self.coefficient_of_variation(data)
        # calculate the weight
        w = v / v.sum()
        # use the filter array to filter the index
        pos = (pos_neg + 1) / 2
        neg = (1 - pos_neg) / 2
        # calculate the compliance of positive index
        g_pos = np.divide(data, target)
        g_pos = g_pos * pos
        # calculate the compliance of negative index
        g_neg = np.divide(target, data)
        g_neg = g_neg * neg
        # add to get the final compliance matrix
        g = g_pos + g_neg
        # convert nan into zero to avoid error
        g = np.nan_to_num(g)
        # calculate the final result
        cov_rlt = (w * g).sum(axis=1)
        # round the result according to the decimals
        rlt = np.around(cov_rlt, decimals)
        return rlt
