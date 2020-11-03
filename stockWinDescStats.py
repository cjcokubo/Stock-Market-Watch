# Author: Christine Okubo
# Date: 10-23-20
# Inputs: 1) input dataset with stock prices over time, 2) flag*, 3) window size (ex: n=14 for 14-day window)
# *flag: 1 = mean, 2 = SD and 3 = correlation
# Outputs: 1) array with mean, sd, or correlation of stock prices for a given window of time, 2) plot

def stockWinDescStats (input_array, flag, window):
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.stats import pearsonr
    input_length = len(input_array)
    
    # Mean
    if (flag == 1):
        mean_array = np.array([])
        for i in range(input_length - window + 1):
            lst = np.array(input_array[i:i+window])
            mean = np.mean(lst)
            mean_array = np.append(mean_array, mean)
        plt.plot(mean_array)
        plt.show()
        return mean_array
    
    # Standard Deviation
    elif (flag == 2):
        std_array = np.array([])
        for i in range(input_length - window + 1):
            lst = np.array(input_array[i:i+window])
            std = np.std(lst)
            std_array = np.append(std_array, std)
        plt.plot(std_array)
        plt.show()
        return std_array
    
    # Correlation
    elif (flag == 3):
        transposed_array = np.transpose(input_array)
        
        first_array = transposed_array[0]
        second_array = transposed_array[1]
        
        r_array = np.array([])
        for i in range(first_array.size - window + 1):
            first_lst = np.array(first_array[i:i+window])
            second_lst = np.array(second_array[i:i+window])
            
            r = pearsonr(first_lst, second_lst)
            r_array = np.append(r_array, r[0])
        plt.plot(r_array)
        plt.show()
        return r_array
    
    else:
        print("Please enter a valid flag.")
    