def data_anya():
    import pandas as pd
    import numpy as np
    import os
    import math
    from data_extraction_pw_hbond_anya import source1df

    folder_path = 'Data'
    temps = ['t3', 't3', 't3', 't3', 't3', 't20', 't20', 't20', 't20', 't37', 't37', 't37', 't37', 't37']
    phs = ['1', '2', '3', '4', '5', '1', '3', '4', '5', '1', '2', '3', '4', '5']
    metric = 'hbond'
    include = 'p-w'
    exclude2 = 'side'
    # Call extracted data from source 1
    source1df = source1df()

    all_data = []
    all_colnames = []
    for t in temps:
        for p in phs:
            # Get into subfolder
            cur_path = folder_path + '/' + t + '-' + p
            cur_column = t + '-' + p
            if os.path.exists(cur_path):
                # Get all hbond files, excluding hbond-p-w and hbond-side
                file_names = []
                for file in os.listdir(cur_path):
                    if metric in file and include in file and not exclude2 in file:
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
                                        if '.050' in vals[i]:
                                            nums.append(round(float(vals[i]) + 0.0001,1))
                                        else:
                                            nums.append(round(float(vals[i]),1))
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
                    if not math.isclose(cur_file_data[0][0] - last_timestamp, 0.1):
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

    # Determine which dataframe has more times and append the dataframes based on time column size (greater column size appended first)
    # Source 2 has more times than source 1
    if len(df["Time"]) > len(source1df["Time"]):
        # Drop the time column of source 1
        source1df.drop('Time', inplace = True, axis = 1)
        # Merge extracted data from source 1 and source 2 so that source 2's data is first, including its time values
        df_anya = pd.concat([df, source1df], axis = 1)
    # Source 1 has more times than source 2    
    else:
        # Drop the time column of source 2
        df.drop('Time', inplace = True, axis = 1)
        # Merge extracted data from source 1 and source 2 so that source 1's data is first, including its time values
        df_anya = pd.concat([source1df, df], axis = 1)
    return df_anya