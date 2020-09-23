# All decimal 3 places

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
    return median_value


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    # Standard deviation Logic
    return standard_deviation_value


# Function to compute variance. You cant use Python functions
def variance(first_list):
    # variance Logic

    return variance_value


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    # RMSE Logic
    return rmse_value


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    # mse Logic
    return mse_value


# Function to compute mae. You cant use Python functions
def mae(first_list, second_list):
    # mae Logic
    return mae_value


# Function to compute NSE. You cant use Python functions
def nse(first_list, second_list):
    # nse Logic
    return nse_value


# Function to compute Pearson correlation coefficient. You cant use Python functions
def pcc(first_list, second_list):
    # nse Logic
    return pcc_value


# Function to compute Skewness. You cant use Python functions
def skewness(first_list):
    # Skewness Logic
    return skewness_value


def sorting(first_list):
    # Sorting Logic
    # Selection sorting
    for element in first_list:
        if not isinstance(element, (int, float)):
            return 0
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


print(sorting([0.558, 0.641, 0.302, 0.091, -0.389, -
               1.003, 0.475, 0.226, 0.404, -1.108, 0.051, 0, 0, 0]))
