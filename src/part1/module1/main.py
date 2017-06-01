# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



#
#  构建“用户----产品 二分网 
#   度和度分布
#       1.	对网络中所有节点的度求平均，得到网络的平均度 ，即把所有节点的度相加再除以节点数， 得到一个数值。
#       2.	画出网络度分布图：横坐标为度K，纵坐标为节点的度为K的概率。 为网络中度为 的节点在整个网络中所占的比率，也就是，在网络中随机抽取到度为 的节点的概率为
#   



if __name__ == '__main__':
    
  
    f = open('log.txt','w')	
    dataSet = "../../../data/100W_UTF8.csv"
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

    # pos = nx.spring_layout(G)
    # nx.draw_networkx(G, pos, with_labels=False,node_size=1, width=0.1, edge_color='black', dpi=1024, figsize=2048)
    # plt.savefig("../../../target/用户-产品-二分网络图.png",dpi=1024,figsize=1024)
    # # plt.show()

    print("graph info:", nx.info(G), file=f)
    g_nodes = G.number_of_nodes()
    g_edges = G.number_of_edges()
    g_sum_nodes = sum(G.degree().values())
    # g_shortest_path = nx.diameter(G)
    # g_average_shortest_path = nx.average_shortest_path_length(G)
    # g_clustering = nx.clustering(G) # 字典格式
    # g_average_clustering = nx.average_clustering(G)
    # print("G average_clustering ->", g_average_clustering, file=f)
    # print("G clustering ->", g_clustering, file=f)


    degree = nx.degree_histogram(G)  # 来返回一个表示度分布频率的list，list的元素代表度的数量，在list中的index表示度数
    x = range(len(degree))
    y = [z/float(sum(degree)) for z in degree]


    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit) 
    # fit_fn is now a function which takes in x and returns an estimate for y

    # plt.plot(x,y, 'yo', x, fit_fn(x), '--k',markersize = 10, marker='.')

    plt.plot(x, y,'yo',markersize=10, marker='.')
    plt.xlabel('degree')
    plt.ylabel('degree P(K)')
    plt.savefig("../../../target/度和度分布.png",dpi=1024,figsize=1024)

    plt.loglog(x, y,'yo',x, fit_fn(x), '--k',markersize = 10, marker='.')
    # plt.xlabel('degree')
    # plt.ylabel('degree P(K)')
    # plt.xlim(0,100)
    plt.savefig("../../../target/度和度分布-双log图.png",dpi=1024,figsize=1024)