# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



#
#  构建“用户----产品 二分网 



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
    product = nx.project(G, set(loan_id_nodes))  # 向product节点投影

   
    # 单顶点产品
    G2 = bipartite.projected_graph(G, product)
    # nx.draw_networkx(G1, pos)
    # plt.show()
    print(nx.info(G2),file=f)
    g2_nodes = G2.number_of_nodes()
    g2_sum_nodes = sum(G2.degree().values())
    # g2_clustering = nx.clustering(G2)
    g2_average_degree = (float(g2_sum_nodes)/float(g2_nodes))
    g2_average_clustering = nx.average_clustering(G2)
    g2_shortest_path = min(nx.all_pairs_shortest_path(G2))
    # print("G2 clustering ->", g2_clustering,file=f)
    print("G2 average_clustering ->", g2_average_clustering,file=f)
    print("G2 average_degree->", g2_average_degree,file=f)
    print("G2 shortest path->", g2_shortest_path,file=f)


    pos = nx.spring_layout(G2)
    nx.draw_networkx(G2, pos, with_labels=False,node_size=1, width=0.1, edge_color='black',dpi=1024, figsize=2048)
    plt.savefig("../../../target/产品网.png",dpi=1024,figsize=1024)