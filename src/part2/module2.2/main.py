# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



#
#  只有出度用户



if __name__ == '__main__':
    
  
    f = open('../../../logs/part2-module2.2.log','w')	
    dataSet = "../../../data/10W_UTF8.csv"
    print("loading data....", dataSet, file=f)
    data = pd.read_csv(dataSet)
    print(data.info(),file=f)
    print("size of dataset :", data.size, file=f)
    print("shape of dataset :", data.shape, file=f)
    print("length of data set :", len(data),file=f)
    print(data.columns,file=f)

   
    G1 = nx.DiGraph()
    G2 = nx.Graph()
    tenderer_nodes = []
    loan_id_nodes = []
    out_users = []
    loaner_name_list = []
    for i in range(len(data)):
        
        loan_id = data.get_value(i, 'loanid')
        loaner_name = data.get_value(i, 'loaner_name')
        tender_name = data.get_value(i, 'tender_name')
        product_amount = data.get_value(i, 'loan_rate')
        
        G1.add_node(tender_name)  
        G1.add_node(loaner_name)
        G1.add_weighted_edges_from([(tender_name, loaner_name, 1.0)])

        G2.add_node(tender_name)  
        G2.add_node(loan_id, amount=product_amount)
        G2.add_weighted_edges_from([(tender_name, loan_id, 1.0)])

        tenderer_nodes.append(tender_name)
        loan_id_nodes.append(loan_id)
        loaner_name_list.append(loaner_name)


    node_list = G1.nodes()
    for node in node_list:
        in_degree = G1.in_degree(node)
        out_degree =  G1.out_degree(node)
        if(out_degree >0 and in_degree<=0):
            out_users.append(node)

    user_list = list(set(tenderer_nodes) - set(out_users))
    G2.remove_nodes_from(user_list)

    # # 投影
    NSet = bipartite.sets(G2)
    user = nx.project(G2, set(out_users))  # 向user节点投影
    product = nx.project(G2, set(loan_id_nodes))  # 向product节点投影


    
    G3 = bipartite.projected_graph(G2, product)
 

    degrees = nx.degree(G3)
    attribute_clust = {}
    ave_degree_dict = {}


    print("product graph info:", nx.info(G3), file=f)
    for product_node in G3.nodes():
        degree = degrees.get(product_node)
        attribute = G3.node[product_node].get('amount')
        print("attribute:", attribute, file=f)
        print("degree:", degree, file=f)
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
    plt.xlabel('rate')
    plt.ylabel('avg degree')
    plt.title('out degree user')
    plt.grid(True)
    plt.savefig("../../../target/出度用户-产品网利率和平均度.png",dpi=1024,figsize=1024)


    plt.loglog(x, y,'yo',markersize = 5, marker='.')
    plt.grid(True)
    plt.xlabel('rate')
    plt.ylabel('avg degree')
    plt.title('out degree user')
    plt.savefig("../../../target/出度用户-产品网利率和平均度-双log图.png",dpi=1024,figsize=1024)