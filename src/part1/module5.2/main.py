# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



#
#  构建“用户----产品 二分网 



if __name__ == '__main__':
    f = open('../../../logs/part1-module5.2.log','w')	
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
  


    degrees = nx.degree(G1)
    clusters = nx.clustering(G1)
    nodes = G1.nodes()
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

    x = list(deg_avg_clust.keys())
    y = list(deg_avg_clust.values())
    plt.plot(x, y,'ro', markersize = 5, marker='.')
    plt.xlabel('degree')
    plt.ylabel('avg custer')
    plt.grid(True)
    plt.savefig("../../../target/产品网度和群聚系数.png",dpi=1024,figsize=1024)


    plt.loglog(x, y,'ro', markersize = 5, marker='.')
    plt.xlabel('degree')
    plt.ylabel('avg custer')
    plt.grid(True)
    plt.savefig("../../../target/产品网度和群聚系数-双log图.png",dpi=1024,figsize=1024)