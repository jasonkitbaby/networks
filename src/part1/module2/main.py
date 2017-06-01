# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite


#  构建“用户----产品 二分网 
#   集聚系数与聚度相关性
#       1. 计算得到网络的平均集聚系数C, 计算的是网络中与同一个节点连接的两节点之间也相互连接的平均概率。得到一个数值。
#       2. 计算具有相同规模的随机网络的平均聚集系数。。得到一个数值。
#       3. 在求得各节点集聚系数的基础上，可以得到度为 的节点的集聚系数的平均值 ，

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
    # g_clustering = nx.clustering(G) # 字典格式
    print("G average_clustering ->", g_average_clustering, file=f)
    # print("G clustering ->", g_clustering, file=f)

    degrees = nx.degree(G)
    clusters = nx.clustering(G)
    nodes = G.nodes()
    deg_clust = {}
    deg_avg_clust = {}
    for node in nodes:
        print("Node :", node, file=f)
        degree = degrees.get(node) 
        cluster = clusters.get(node)
        print("Node degree:", degree, file=f)
        print("Node cluster:", cluster, file=f)
        if(deg_clust.get(degree) == None):
            deg_clust[degree] = [cluster]
        else:
            deg_clust[degree].append(cluster)
    for key in deg_clust.keys():
        deg_clusters = deg_clust[key]
        avg_cluster = sum(deg_clusters)/len(deg_clusters)
        deg_avg_clust[key] = avg_cluster

    print(deg_avg_clust.keys())
    print(deg_avg_clust.values())
    # plt.plot(x, y)
    # plt.xlabel('degree')
    # plt.ylabel('avg custer')
    # plt.savefig("../../../target/度和群聚系数.png",dpi=1024,figsize=1024)
