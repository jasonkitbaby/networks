# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd



# 一. 度和度分布
# 1.	对网络中所有节点的度求平均，得到网络的平均度，即把所有节点的度相加再除以节点数， 得到一个数值。
# 2.	画出网络度分布图：横坐标为度K，纵坐标为节点的度为K的概率。
#       为网络中度为的节点在整个网络中所占的比率，也就是，在网络中随机抽取到度为的节点的概率为，
#       即，x:度，y:度的概率

if __name__ == '__main__':

    f = open('log.txt','w')	
    dataSet = "../../data/1W_UTF8.csv"
    print("loading data....", dataSet, file=f)
    data = pd.read_csv(dataSet)
    print(data.info(),file=f)
    print("size of dataset :", data.size, file=f)
    print("shape of dataset :", data.shape, file=f)
    print("length of data set :", len(data),file=f)
    print(data.columns,file=f)

    
    nodes = []
    for i in range(len(data)):
        load_id = data.get_value(i,'loanid')
        tender_name = data.get_value(i,'tender_name')
        element = (tender_name,load_id)
        nodes.append(element)
    
   
    print("building graph")
    G = nx.Graph()
    G.add_edges_from(nodes)
    # draw 二分无向图
    # pos = nx.shell_layout(G)
    # nx.draw_networkx(G, pos)
    # plt.show()

    print("graphinfo:", nx.info(G), file=f)
    g_nodes = G.number_of_nodes()
    g_sum_nodes = sum(G.degree().values())
    # g_shortest_path = nx.diameter(G)
    # g_average_shortest_path = nx.average_shortest_path_length(G)
    g_clustering = nx.clustering(G)
    g_average_degree = (float(g_sum_nodes)/float(g_nodes))
    g_average_clustering = nx.average_clustering(G)
    print("G average_clustering ->", g_average_clustering, file=f)
    print("G clustering ->", g_clustering, file=f)
    print("G average_degree->", g_average_degree, file=f)

    degree = nx.degree_histogram(G)
    x = range(len(degree))
    y = [z/float(sum(degree)) for z in degree]
    plt.loglog(x, y)
    plt.savefig("main.png")
    # plt.show()