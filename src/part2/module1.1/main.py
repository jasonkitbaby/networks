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
    
  
    f = open('../../../logs/part2-module1.1.log','w')	
    dataSet = "../../../data/2W_UTF8.csv"
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
    loan_rate_list = []
    loan_term_list = []
    level_value_list = []
    for i in range(len(data)):
        loan_id = data.get_value(i, 'loanid')
        tender_name = data.get_value(i, 'tender_name')
        product_amount = data.get_value(i,'product_amount')
        loan_rate = data.get_value(i,'loan_rate')
        loan_term =  data.get_value(i,'loan_term')
        level_value = data.get_value(i,'level_value');

        loan_id_list.append(loan_id)
        tender_name_list.append(tender_name)
        product_amount_list.append(product_amount)


        G.add_node(tender_name,node_color='r')
        G.add_node(loan_id,node_color='g',amount=product_amount)
        G.add_weighted_edges_from([(tender_name, loan_id, 1.0)])



    print("graph info:", nx.info(G), file=f)

    for amount in  product_amount_list:
        amount_nodes = G.nodes(amount)
        print(amount_nodes, file=f)
