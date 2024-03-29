# All decimal 3 places
from math import *
import os
os.system('cls')

# Function to compute mean


def mean(first_list):
    # mean Logic
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    summation_value = summation(first_list)
    mean_value = round(summation_value/len(first_list), 6)
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
        median_value = round(sorted_list[median_index-1], 6)
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
    mean_of_xi = mean(first_list)
    list_for_summation = []
    for xi in first_list:
        list_for_summation.append(power(xi-mean_of_xi, 2))
    variance_value = summation(list_for_summation)/length
    standard_deviation_value = round(sqrt(variance_value), 6)
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
        list_for_summation.append(power(xi-mean_of_xi, 2))
    variance_value = round(summation(list_for_summation)/length, 6)
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
    list_for_summation = []
    for xi, yi in zip(first_list, second_list):
        list_for_summation.append(power(xi-yi, 2))
    mse_value = summation(list_for_summation)/len(first_list)
    rmse_value = round(sqrt(mse_value), 6)
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
        list_for_summation.append(power(xi-yi, 2))
    mse_value = round(summation(list_for_summation)/len(first_list), 6)
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
    mae_value = round(summation(list_for_summation)/len(first_list), 6)
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
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
        list_for_summation.append(power(xi-yi, 2))
    mse_value = summation(list_for_summation)/len(first_list)
    numerator = mse_value
    denominator = power(standard_deviation(first_list), 2)
    nse_value = round(1-(numerator/denominator), 6)
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
    pcc_value = round(numerator/denominator, 6)
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
        list_for_summation.append(power(xi-mean_of_xi, 3))
    numerator = summation(list_for_summation)
    denominator = length*power(standard_deviation(first_list), 3)
    skewness_value = round(numerator/denominator, 6)
    return skewness_value


def sorting(first_list):
    # Sorting Logic
    # Selection sorting
    length = len(first_list)
    sorted_list = first_list.copy()
    for i in range(length-1):
        index_of_min = i
        for j in range(i+1, length):
            if sorted_list[index_of_min] > sorted_list[j]:
                index_of_min = j
        sorted_list[i], sorted_list[index_of_min] = sorted_list[index_of_min],  sorted_list[i]
    return sorted_list


# Function to compute Kurtosis. You cant use Python functions
def kurtosis(first_list):
    # Kurtosis Logic
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
    length = len(first_list)
    list_for_summation = []
    mean_of_xi = mean(first_list)
    for xi in first_list:
        list_for_summation.append((xi-mean_of_xi)**4)
    numerator = summation(list_for_summation)
    denominator = length*power(variance(first_list), 2)
    kurtosis_value = round(numerator/denominator, 6)
    return kurtosis_value


# Function to compute sum. You cant use Python functions
def summation(first_list):
    # sum Logic
    summation_value = 0
    for element in first_list:
        summation_value += element
    return summation_value


def power(a, b):
    if b == 1:
        return a
    else:
        return a*power(a, b-1)
