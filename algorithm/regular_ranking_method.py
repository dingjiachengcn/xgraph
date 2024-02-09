import time
import logging

# 配置日志
logging.basicConfig(filename='/home/ubuntu/PycharmProjects/xgraph/logs/analysis.log',  # 日志文件路径
                    level=logging.INFO,  # 日志级别
                    format='%(asctime)s - %(levelname)s - %(message)s',  # 日志格式
                    filemode='a')  # 追加模式

def parse_file_to_dict(filepath):
    result = {}
    with open(filepath, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split()
            source_hostname = parts[0]
            source_IP = parts[1].strip("()")
            destination_hostname = parts[3]
            destination_IP = parts[4].strip("()")
            flowCnt = int(parts[5].strip('[]'))
            date = parts[-1]

            key = f"{source_hostname} ({source_IP}) -> {destination_hostname} ({destination_IP}) on {date}"
            result[key] = flowCnt
    return result

def compare_and_rank_changes(file1, file2):
    data_day1 = parse_file_to_dict(file1)
    data_day2 = parse_file_to_dict(file2)
    changes = []

    for key in data_day2:
        if key in data_day1:
            change = data_day2[key] - data_day1[key]
            if change > 0:
                changes.append((key, change))
        else:
            changes.append((key, data_day2[key]))

    changes.sort(key=lambda x: x[1], reverse=True)
    return changes

# 文件路径
file1 = '/home/ubuntu/PycharmProjects/xgraph/src/txt_converted/2023-05-04.txt'
file2 = '/home/ubuntu/PycharmProjects/xgraph/src/txt_converted/2023-05-05.txt'

# 开始计时
start_time = time.time()

changes = compare_and_rank_changes(file1, file2)
for change in changes[:10]:
    logging.info(f"{change[0]}: Increase in flowCnt = {change[1]}")

# 结束计时并记录运行时间
end_time = time.time()
logging.info(f"Process finished in {end_time - start_time} seconds.")
