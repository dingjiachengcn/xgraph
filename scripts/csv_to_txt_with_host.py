import pandas as pd
import os


def csv_to_txt_with_hosts(csv_file_path, txt_file_path):
    # 读取CSV文件
    df = pd.read_csv(csv_file_path)

    # 打开TXT文件准备写入
    with open(txt_file_path, 'w') as txt_file:
        # 遍历DataFrame的每一行
        for index, row in df.iterrows():
            line = f"{row['source_hostname']} ({row['source_IP']}) -> {row['destination_hostname']} ({row['destination_IP']}) [{row['flowCnt']}] on {row['date']}\n"
            txt_file.write(line)


# 文件夹路径
csv_folder_path = '/home/ubuntu/PycharmProjects/xgraph/src/date_split_csvs'
txt_folder_path = '/home/ubuntu/PycharmProjects/xgraph/src/txt_converted'

# 如果TXT文件夹不存在，创建它
if not os.path.exists(txt_folder_path):
    os.makedirs(txt_folder_path)

# 遍历CSV文件夹中的所有文件
for filename in os.listdir(csv_folder_path):
    if filename.endswith('.csv'):
        # 构建完整的CSV文件路径
        csv_file_path = os.path.join(csv_folder_path, filename)
        # 构建对应的TXT文件路径，文件名与CSV相同，扩展名不同
        txt_file_name = os.path.splitext(filename)[0] + '.txt'
        txt_file_path = os.path.join(txt_folder_path, txt_file_name)
        # 转换CSV到TXT
        csv_to_txt_with_hosts(csv_file_path, txt_file_path)

print("所有CSV文件已转换为TXT文件。")
