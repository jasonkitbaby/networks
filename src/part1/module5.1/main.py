# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



#
#  用户网
#  度和度分布
#       1.	对网络中所有节点的度求平均，得到网络的平均度 ，即把所有节点的度相加再除以节点数， 得到一个数值。
#       2.	画出网络度分布图：横坐标为度K，纵坐标为节点的度为K的概率。 为网络中度为 的节点在整个网络中所占的比率，也就是，在网络中随机抽取到度为 的节点的概率为




if __name__ == '__main__':
    f = open('log.txt','w')	
    dataSet = "../../../data/2W_UTF8.csv"
    print("loading data....", dataSet, file=f)
    data = pd.read_csv(dataSet)
    print(data.info(),file=f)
    print("size of dataset :", data.size, file=f)
    print("shape of dataset :", data.shape, file=f)
    print("length of data set :", len(data),file=f)
    print(data.columns,file=f)

    G = nx.Graph()
    tenderer_nodes = []
    loan_id_nodes = []
    for i in range(len(data)):
        loan_id = data.get_value(i, 'loanid')
        tender_name = data.get_value(i, 'tender_name')
        G.add_node(tender_name,node_color='r')
        tenderer_nodes.append(tender_name)
        G.add_node(loan_id,node_color='b')
        loan_id_nodes.append(loan_id)
        G.add_weighted_edges_from([(tender_name, loan_id, 1.0)])

    # pos = nx.spring_layout(G)
    # nx.draw_networkx(G, pos, with_labels=False,node_size=1, width=0.1, edge_color='black',dpi=1024, figsize=2048)
    # plt.savefig("../../../target/用户-产品-二分网络图.png",dpi=1024,figsize=1024)
    # plt.show()

    print("graph info:", nx.info(G), file=f)
    g_nodes = G.number_of_nodes()
    g_edges = G.number_of_edges()
    g_sum_nodes = sum(G.degree().values())
   

    # # 投影
    NSet = bipartite.sets(G)
    user = nx.project(G, set(tenderer_nodes))  # 向user节点投影
    product = nx.project(G, set(loan_id_nodes))  # 向product节点投影

    # 单顶点用户
    G1 = bipartite.projected_graph(G, product)
    # nx.draw_networkx(G1, pos)
    # plt.show()
    print(nx.info(G1),file=f)
  


    degree = nx.degree_histogram(G1)  # 来返回一个表示度分布频率的list，list的元素代表度的数量，在list中的index表示度数
    x = range(len(degree))
    y = [z/float(sum(degree)) for z in degree]

    plt.plot(x, y,'ro')
    plt.xlabel('degree')
    plt.ylabel('degree P(K)')
    plt.grid(True)
    plt.savefig("../../../target/产品网-度和度分布.png",dpi=1024,figsize=1024)

    plt.loglog(x, y,'ro')
    # plt.xlabel('degree')
    # plt.ylabel('degree P(K)')
    # plt.xlim(0,100)
    plt.grid(True)
    plt.savefig("../../../target/产品-度和度分布-双log图.png",dpi=1024,figsize=1024)
