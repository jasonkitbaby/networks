# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite


#
#
#  两个单顶点网络进行统计计算
#  平均度、最短路径长度和聚类系数统计值

if __name__ == '__main__':
    f = open('log.txt','w')	
    dataSet = "../../data/2W_UTF8.csv"
    print("loading data....", dataSet, file=f)
    data = pd.read_csv(dataSet)
    print(data.info(),file=f)
    print("size of dataset :", data.size, file=f)
    print("shape of dataset :", data.shape, file=f)
    print("length of data set :", len(data),file=f)
    print(data.columns,file=f)

    G = nx.Graph()
    for i in range(len(data)):
        loan_id = data.get_value(i,'loanid')
        tender_name = data.get_value(i,'tender_name')
        G.add_node(tender_name)
        # 添加节点product_id
        G.add_node(loan_id)
        # 添加边
        # G.add_edge(tenderer, loan_id)
        G.add_weighted_edges_from([(tender_name, loan_id, 1.0)])


    # nodes = []
    # for i in range(len(data)):
    #     load_id = data.get_value(i,'loanid')
    #     tender_name = data.get_value(i,'tender_name')
    #     element = (tender_name,load_id)
    #     nodes.append(element)

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos,with_labels=False,node_size=1,width=0.1,edge_color='black', node_color=('green','red'),dpi=1024,figsize=2048)
    plt.savefig("main.png",dpi=1024,figsize=1024)
    # plt.show()

    print("graph info:", nx.info(G), file=f)
    g_nodes = G.number_of_nodes()
    g_edges = G.number_of_edges()
    g_sum_nodes = sum(G.degree().values())
    # g_shortest_path = nx.diameter(G)
    # g_average_shortest_path = nx.average_shortest_path_length(G)
    g_clustering = nx.clustering(G) # 字典格式
    g_average_clustering = nx.average_clustering(G)
    print("G average_clustering ->", g_average_clustering, file=f)
    print("G clustering ->", g_clustering, file=f)

    # # 投影
    # NSet = bipartite.sets(G)
    # user = nx.project(G, set(tenderer_nodes))  # 向user节点投影
    # product = nx.project(G, set(loan_id_nodes))  # 向product节点投影

    # # 单顶点用户
    # G1 = bipartite.projected_graph(G, user)
    # nx.draw_networkx(G1, pos)
    # plt.show()
    # print nx.info(G1)
    # g1_nodes = G1.number_of_nodes()
    # g1_sum_nodes = sum(G1.degree().values())
    # # g1_shortest_path = nx.diameter(G1)
    # # g1_average_shortest_path = nx.average_shortest_path_length(G1)
    # g1_shortest_path = min(nx.all_pairs_shortest_path(G1))
    # g1_clustering = nx.clustering(G1)
    # g1_average_degree = (float(g1_sum_nodes)/float(g1_nodes))
    # g1_average_clustering = nx.average_clustering(G1)
    # print("G1 average_clustering ->", g1_average_clustering)
    # print("G1 clustering ->", g1_clustering)
    # print("G1 average_degree->", g1_average_degree)
    # print("G1 shortest path->", g1_shortest_path)

    # # 单顶点产品
    # G2 = bipartite.projected_graph(G, product)
    # nx.draw_networkx(G1, pos)
    # plt.show()
    # print nx.info(G2)
    # g2_nodes = G2.number_of_nodes()
    # g2_sum_nodes = sum(G2.degree().values())
    # g2_clustering = nx.clustering(G2)
    # g2_average_degree = (float(g2_sum_nodes)/float(g2_nodes))
    # g2_average_clustering = nx.average_clustering(G2)
    # g2_shortest_path = min(nx.all_pairs_shortest_path(G1))
    # print("G2 clustering ->", g2_clustering)
    # print("G2 average_clustering ->", g2_average_clustering)
    # print("G2 average_degree->", g2_average_degree)
    # print("G2 shortest path->", g2_shortest_path)