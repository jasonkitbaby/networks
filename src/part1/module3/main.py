# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite


#  构建“用户----产品 二分网 
#   网络平均最短路径
# 1.	计算得到网络的平均最短路径L, 两节点之间的最短路径为：节点A到节点B所要经历的边的最小数目。网络的平均距离为所有节点对之间距离的平均值。得到一个数值
# 2. 计算具有相同规模的随机网络的平均最短路径。得到一个数值。


if __name__ == '__main__':
    f = open('log.txt','w')	
    dataSet = "../../../data/1W_UTF8.csv"
    print("loading data....", dataSet, file=f)
    data = pd.read_csv(dataSet)
    print(data.info(),file=f)
    print("size of dataset :", data.size, file=f)
    print("shape of dataset :", data.shape, file=f)
    print("length of data set :", len(data),file=f)
    print(data.columns,file=f)

    G = nx.Graph()
    for i in range(len(data)):
        loan_id = data.get_value(i, 'loanid')
        tender_name = data.get_value(i, 'tender_name')
        G.add_node(tender_name)
        G.add_node(loan_id)
        G.add_weighted_edges_from([(tender_name, loan_id, 1.0)])

    print("graph info:", nx.info(G), file=f)
    g_average_clustering = nx.average_clustering(G)
    g_clustering = nx.clustering(G) # 字典格式

    # path=nx.all_pairs_shortest_path(G)    
    # g_diameter = nx.diameter(G) #@返回图G的直径（最长最短路径的长度），
    # g_shortest_path_length = nx.average_shortest_path_length(G)#则返回图G所有节点间平均最短路径长度。
    print("G average_clustering ->", g_average_clustering, file=f)
    print("G clustering ->", g_clustering, file=f)
    # print("G path ->", path, file=f)
    # print("G g_shortest_path_length ->", g_shortest_path_length, file=f)

