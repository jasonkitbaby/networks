# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import logging  
import logging.handlers 


# 二 集聚系数与聚度相关性
# 1. 计算得到网络的平均集聚系数C, 计算的是网络中与同一个节点连接的两节点之间也相互连接的平均概率。得到一个数值。
# 2. 计算具有相同规模的随机网络的平均聚集系数。。得到一个数值。
# 3. 在求得各节点集聚系数的基础上，可以得到度为的节点的集聚系数的平均值，绘制下方统计图
# 4. 进一步再把上图画在双对数坐标下
# x:度， y:度的群聚系数
if __name__ == '__main__':
    

    f = open('log.txt','w')	
    dataSet = "../../data/1W_UTF8.csv"
    print("loading data....", dataSet , file=f)
    data = pd.read_csv(dataSet)
    print("data info:", data.info(), file=f)
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

    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw_networkx(G, pos,with_labels=False,node_size=1,width=0.5,edge_color='black',dpi=1024,figsize=2048)
    plt.savefig("main.png",dpi=600,figsize=1024)
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

    # G_tmp = nx.random_graphs.barabasi_albert_graph(g_edges,g_nodes)
    # g_tmp_clustering = nx.clustering(G_tmp)
    # g_tmp_average_clustering = nx.average_clustering(G_tmp)
    # print("G_tmp average_clustering ->", g_tmp_average_clustering, file=f)
    # print("G_tmp clustering ->", g_tmp_clustering, file=f)

    # dict = {}
    # x = []
    # y = []
    # for key in g_clustering.keys():
    #     node_degree = G.degree(key)
    #     print(G.degree(key),file=f)
    #     print(g_clustering[key],file=f)


    # plt.loglog(x, y)
    # plt.savefig("main2.png")
    # plt.show()