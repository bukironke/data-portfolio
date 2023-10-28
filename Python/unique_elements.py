def get_clean_data (data_list):
    clean_data = []
    for num in data_list:
        if num not in clean_data:
            clean_data.append(num)
    return clean_data

data_list = [1, 5, 2000, 1343, 200, 3000, 2000, 1344, 2345, 9829]
output_list = get_clean_data(data_list)
print (output_list)
