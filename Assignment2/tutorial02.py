# All decimal 3 places
from math import *
import numpy as np
# Function to compute mean


def mean(first_list):
    # mean Logic
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    summation_value = summation(first_list)
    mean_value = round(summation_value/len(first_list), 3)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):
    # median Logic
    length = len(first_list)
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    sorted_list = sorting(first_list)
    if length % 2 == 1:
        median_index = int((length + 1)/2)
        median_value = round(sorted_list[median_index-1], 3)
    else:
        median_ind_list = [int(length/2), int(length/2 + 1)]
        median_list = [sorted_list[median_ind_list[0]-1],
                       sorted_list[median_ind_list[1]-1]]
        median_value = mean(median_list)
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    length = len(first_list)
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    var = variance(first_list)
    standard_deviation_value = round(sqrt(var), 3)
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic
    length = len(first_list)
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    mean_of_xi = mean(first_list)
    list_for_summation = []
    for xi in first_list:
        list_for_summation.append((xi-mean_of_xi)**2)
    variance_value = round(summation(list_for_summation)/length, 3)
    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    if len(second_list) != len(first_list):
        return 0
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    for element in second_list:
        if not isinstance(element, (int, float)):
            return 0
    mse_value = mse(first_list, second_list)
    rmse_value = round(sqrt(mse_value), 3)
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    if len(second_list) != len(first_list):
        return 0
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    for element in second_list:
        if not isinstance(element, (int, float)):
            return 0
    list_for_summation = []
    for xi, yi in zip(first_list, second_list):
        list_for_summation.append((xi-yi)**2)
    mse_value = round(summation(list_for_summation)/len(first_list), 3)
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    if len(second_list) != len(first_list):
        return 0
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    for element in second_list:
        if not isinstance(element, (int, float)):
            return 0
    list_for_summation = []
    for xi, yi in zip(first_list, second_list):
        list_for_summation.append(abs(xi-yi))
    mae_value = round(summation(list_for_summation)/len(first_list), 3)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    if len(second_list) != len(first_list):
        return 0
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    for element in second_list:
        if not isinstance(element, (int, float)):
            return 0
    length = len(first_list)
    list_for_summation = []
    mean_of_xi = mean(first_list)
    mean_of_yi = mean(second_list)
    for xi, yi in zip(first_list, second_list):
        list_for_summation.append((xi-mean_of_xi)*(yi-mean_of_yi))
    numerator = summation(list_for_summation)
    denominator = standard_deviation(
        first_list)*standard_deviation(second_list)*length
    pcc_value = round(numerator/denominator, 3)
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    length = len(first_list)
    list_for_summation = []
    mean_of_xi = mean(first_list)
    for xi in first_list:
        list_for_summation.append((xi-mean_of_xi)**3)
    numerator = summation(list_for_summation)
    denominator = length*(standard_deviation(first_list)**3)
    skewness_value = round(numerator/denominator, 3)
    return skewness_value


def sorting(first_list):
    # Sorting Logic
    # Selection sorting
    length = len(first_list)
    for i in range(length-1):
        index_of_min = i
        for j in range(i+1, length):
            if first_list[index_of_min] > first_list[j]:
                index_of_min = j
        first_list[i], first_list[index_of_min] = first_list[index_of_min],  first_list[i]
    sorted_list = first_list
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic

    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value = 0
    for element in first_list:
        summation_value += element
    return summation_value
