import pandas as pd

def parse_file_to_dict(filepath):
    result = {}
    with open(filepath, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split()
            # Extracting source and destination info
            source_hostname = parts[0]
            source_IP = parts[1].strip("()")
            destination_hostname = parts[3]
            destination_IP = parts[4].strip("()")
            flowCnt = int(parts[5].strip('[]'))
            date = parts[-1]  # Assuming date is always the last part

            key = f"{source_hostname} ({source_IP}) -> {destination_hostname} ({destination_IP}) on {date}"
            result[key] = flowCnt
    return result



def compare_and_rank_changes(file1, file2):
    data_day1 = parse_file_to_dict(file1)
    data_day2 = parse_file_to_dict(file2)
    changes = []

    # Check for changes and new appearances in day 2 compared to day 1
    for key in data_day2:
        if key in data_day1:
            change = data_day2[key] - data_day1[key]
        else:
            change = data_day2[key]  # New appearance
        changes.append((key, change))

    # Additionally, check for disappearances from day 1 to day 2
    for key in data_day1:
        if key not in data_day2:
            change = -data_day1[key]  # Disappearance
            changes.append((key, change))

    # Sort by absolute change in descending order
    changes.sort(key=lambda x: abs(x[1]), reverse=True)
    return changes

# Update these paths to the actual files
file1 = '/home/ubuntu/PycharmProjects/xgraph/src/txt_converted/2023-05-04.txt'
file2 = '/home/ubuntu/PycharmProjects/xgraph/src/txt_converted/2023-05-05.txt'

changes = compare_and_rank_changes(file1, file2)
for change in changes[:10]:  # Display top 10 changes
    print(f"{change[0]}: Change in flowCnt = {change[1]}")
