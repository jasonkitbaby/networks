# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



#
#  用户兴趣研究

# 1.	横坐标为产品的amount（代表金额），纵坐标为产品的度。
# 2.	横坐标为产品的Rate (代表利息)，纵坐标为产品的度。
# 3.	横坐标为产品的Term (代表周期)，纵坐标为产品的度。
# 4.	横坐标为产品的level (代表产品的风险等级)，纵坐标为产品的度。




if __name__ == '__main__':
    
  
    f = open('../../../logs/part2-module1.3.log','w')	
    dataSet = "../../../data/10W_UTF8.csv"
    print("loading data....", dataSet, file=f)
    data = pd.read_csv(dataSet)
    print(data.info(),file=f)
    print("size of dataset :", data.size, file=f)
    print("shape of dataset :", data.shape, file=f)
    print("length of data set :", len(data),file=f)
    print(data.columns,file=f)

    G = nx.Graph()
    loan_id_list = []
    tender_name_list = []
    product_amount_list = []



    for i in range(len(data)):
        loan_id = data.get_value(i, 'loanid')
        tender_name = data.get_value(i, 'tender_name')
        product_amount = data.get_value(i, 'loan_term')

        loan_id_list.append(loan_id)
        tender_name_list.append(tender_name)
        product_amount_list.append(product_amount)

        G.add_node(tender_name)
        G.add_node(loan_id, amount=product_amount)
        G.add_weighted_edges_from([(tender_name, loan_id, 1.0)])

    print("origin graph info:", nx.info(G), file=f)

    # # 投影
    NSet = bipartite.sets(G)
    user = nx.project(G, set(tender_name_list))  # 向user节点投影
    product = nx.project(G, set(loan_id_list))  # 向product节点投影


    G1 = bipartite.projected_graph(G, product)

    degrees = nx.degree(G1)
    attribute_clust = {}
    ave_degree_dict = {}


    print("product graph info:", nx.info(G1), file=f)
    for product_node in G1.nodes():
        degree = degrees.get(product_node)
        attribute = G1.node[product_node].get('amount')
        # print("amount:", amount, file=f)
        # print("degree:", degree, file=f)
        if(attribute_clust.get(attribute) == None):
                attribute_clust[attribute] = [degree]
        else:
            attribute_clust[attribute].append(degree)

    for key in attribute_clust.keys():
        attribute_degree = attribute_clust[key]
        avg_degree = sum(attribute_degree)/len(attribute_degree)
        ave_degree_dict[key] = avg_degree
    x = list(ave_degree_dict.keys())
    y = list(ave_degree_dict.values())
    plt.plot(x, y,'yo',markersize = 5, marker='.')
    plt.xlabel('loan_term')
    plt.ylabel('avg degree')
    plt.grid(True)
    plt.savefig("../../../target/用户-产品网周期和平均度.png",dpi=1024,figsize=1024)


    plt.loglog(x, y,'yo',markersize = 5, marker='.')
    plt.grid(True)
    plt.xlabel('loan_term')
    plt.ylabel('avg degree')
    plt.savefig("../../../target/用户-产品网周日和平均度-双log图.png",dpi=1024,figsize=1024)