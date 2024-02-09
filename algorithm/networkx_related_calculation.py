import networkx as nx
import time
import logging
import numpy as np

# 配置日志
logging.basicConfig(filename='/home/ubuntu/PycharmProjects/xgraph/logs/analysis.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='a')

def load_directed_graph_from_file(file_path):
    G = nx.DiGraph()
    with open(file_path, 'r') as file:
        next(file)  # Skip header line
        for line in file:
            parts = line.strip().split()
            source = parts[0]
            target = parts[3]
            G.add_edge(source, target)
    return G

def calculate_triangles(G):
    undirected_G = G.to_undirected()
    triangles = sum(nx.triangles(undirected_G).values()) // 3
    return triangles

def calculate_gcd(triangles1, triangles2):
    return abs(triangles1 - triangles2)

def calculate_gcm(triangles1, triangles2):
    # Simplified correlation measure, as we are only dealing with triangle counts
    return np.corrcoef([triangles1, triangles2])[0, 1]

file_paths = ['/home/ubuntu/PycharmProjects/xgraph/src/txt_converted/2023-05-04.txt',
              '/home/ubuntu/PycharmProjects/xgraph/src/txt_converted/2023-05-05.txt']

triangles_counts = []
for file_path in file_paths:
    start_time = time.time()
    G = load_directed_graph_from_file(file_path)
    triangles = calculate_triangles(G)
    triangles_counts.append(triangles)
    end_time = time.time()
    logging.info(f"File: {file_path}, Triangles: {triangles}, Time taken to calculate triangles: {end_time - start_time} seconds")

# Calculate and log GCD and GCM
start_time = time.time()
gcd = calculate_gcd(triangles_counts[0], triangles_counts[1])
end_time = time.time()

logging.info(f"GCD based on triangle counts between the two graphs: {gcd}")
logging.info(f"Time taken to calculate GCD: {end_time - start_time} seconds")
