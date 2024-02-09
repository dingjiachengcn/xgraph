import pandas as pd
import os

# 定义原始CSV文件路径和目标文件夹路径
csv_file_path = '/home/ubuntu/PycharmProjects/xgraph/src/anonymized.csv'
target_folder_path = '/home/ubuntu/PycharmProjects/xgraph/src/date_split_csvs'

# 如果目标文件夹不存在，创建它
if not os.path.exists(target_folder_path):
    os.makedirs(target_folder_path)

# 读取CSV文件
df = pd.read_csv(csv_file_path)

# 根据日期分组，然后保存每个分组到一个新的CSV文件
for date, group in df.groupby('date'):
    # 格式化文件名，将斜杠替换为下划线
    filename = date.replace('/', '_') + '.csv'
    filepath = os.path.join(target_folder_path, filename)
    # 保存分组到CSV文件
    group.to_csv(filepath, index=False)

print("split complete")
