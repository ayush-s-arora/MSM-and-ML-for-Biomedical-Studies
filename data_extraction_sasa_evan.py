def data_evan():
    import pandas as pd
    import numpy as np
    import os

    folder_path = 'Data/dl'
    temps = ['t3', 't20', 't37']
    phs = ['1', '2', '3', '4', '5']
    trials = ['_1', '_2']
    metric = 'sasa'
    #file_names = ['sasa01-26.xvg', 'sasa27-57.xvg', 'sasa01-16.xvg', 'sasa17-37.xvg', 'sasa38-57.xvg']
    #exception = '/t37/t37_1'


    all_data = []
    all_colnames = []
    for t in temps:
        for p in phs:
            for tr in trials:
                # Get into subfolder
                cur_path = folder_path + '/' + t + '/' + p + tr
                cur_column = t + '-' + p + tr
                if os.path.exists(cur_path):
                    # Get all sasa files
                    file_names = []
                    for file in os.listdir(cur_path):
                        if metric in file:
                            file_names.append(file)
                    
                    # Extract numerical data from files
                    all_file_data = []
                    for file in file_names:
                        # Extract data from one file
                        f = open(cur_path + '/' + file, 'r')
                        cur_file_data = []
                        for line in f:
                            if not line.startswith('#') and not line.startswith('@'):
                                line.strip()
                                vals = line.split()
                                nums = []
                                for i in range(len(vals)):
                                    if i == 0:
                                        if '.500' in vals[i]:
                                            nums.append(round(float(vals[i]) + 0.001,0))
                                        else:
                                            nums.append(round(float(vals[i]),0))
                                    else:
                                        nums.append(float(vals[i]))
                                cur_file_data.append(nums)
                        all_file_data.append(cur_file_data)
                    
                    # Sort based on file names
                    # Get first number in file name
                    first_numbers = []
                    for file in file_names:
                        list_string = list(file)
                        for i in range(len(metric)):
                            list_string.pop(0)
                        number = 0
                        i = 0
                        while list_string[i].isdigit():
                            number = number * 10 + int(list_string[i])
                            i += 1
                        first_numbers.append(number)
                    # Selection sort
                    for i in range(len(first_numbers)):
                        smallest_index = i
                        smallest_val = first_numbers[smallest_index]
                        for j in range(len(first_numbers) - i):
                            index = j + i
                            if first_numbers[index] < smallest_val:
                                smallest_index = index
                                smallest_val = first_numbers[index]
                        placeholder = first_numbers[i]
                        first_numbers[i] = first_numbers[smallest_index]
                        first_numbers[smallest_index] = placeholder
                        placeholder = all_file_data[i]
                        all_file_data[i] = all_file_data[smallest_index]
                        all_file_data[smallest_index] = placeholder

                    # Combine the files into one list
                    combined_list = all_file_data[0]
                    for i in range(len(all_file_data) - 1):
                        last_timestamp = combined_list[len(combined_list)-1][0]
                        cur_file_data = all_file_data[i+1]
                        # Remove redundant time stamps
                        while len(cur_file_data) > 0 and cur_file_data[0][0] <= last_timestamp:
                            removed = cur_file_data.pop(0)
                        if (cur_file_data[0][0] - last_timestamp) != 1:
                            print("Error: " + cur_column)
                            print(cur_file_data[0][0])
                            print(last_timestamp)
                        # Combine current data to master data
                        combined_list.extend(cur_file_data)
                    
                    all_data.append(combined_list)
                    all_colnames.append(cur_column)
    # Add all data to a dataframe
    df = pd.DataFrame()

    # Find longest column
    # This will be the length of the entire dataframe
    longest_index = 0
    longest = 0
    for i in range(len(all_data)):
        if len(all_data[i]) > longest:
            longest_index = i
            longest = len(all_data[i])
    times = [all_data[longest_index][i][0] for i in range(len(all_data[longest_index]))]
    df["Time"] = times

    # Add all columns to dataframe
    for i in range(len(all_data)):
        metric_vals = [all_data[i][j][1] for j in range(len(all_data[i]))]
        while len(metric_vals) < longest:
            metric_vals.append(np.NaN)
        df[all_colnames[i]] = metric_vals

    # DATA JUMPS FROM 200-600
    # Sorting method is faulty
    return df