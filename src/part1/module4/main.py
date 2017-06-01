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

    # # 投影
    NSet = bipartite.sets(G)
    user = nx.project(G, set(tenderer_nodes))  # 向user节点投影
    product = nx.project(G, set(loan_id_nodes))  # 向product节点投影

    # 单顶点用户
    G1 = bipartite.projected_graph(G, user)
    # nx.draw_networkx(G1, pos)
    # plt.show()
    print(nx.info(G1),file=f)
    g1_nodes = G1.number_of_nodes()
    g1_sum_nodes = sum(G1.degree().values())
    # g1_diameter = nx.diameter(G1)
    g1_average_shortest_path = nx.average_shortest_path_length(G1)
    g1_shortest_path = min(nx.all_pairs_shortest_path(G1))
    # g1_clustering = nx.clustering(G1)
    g1_average_degree = (float(g1_sum_nodes)/float(g1_nodes))
    g1_average_clustering = nx.average_clustering(G1)
    print("G1 average_clustering ->", g1_average_clustering,file=f)
    # print("G1 clustering ->", g1_clustering,file=f)
    print("G1 average_degree->", g1_average_degree,file=f)
    print("G1 shortest path->", g1_shortest_path,file=f)
    print("G1 g1_average_shortest_path path->", g1_average_shortest_path,file=f)
    # print("G1 g1_diameter path->", g1_diameter,file=f)
    
    # pos = nx.spring_layout(G1)
    # nx.draw_networkx(G1, pos, with_labels=False,node_size=1, width=0.1, edge_color='black',dpi=1024, figsize=2048)
    # plt.savefig("../../../target/用户网.png",dpi=1024,figsize=1024)

