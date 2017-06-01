# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



#
#  只有出度用户



if __name__ == '__main__':
    
  
    f = open('../../../logs/part2-module2.log','w')	
    dataSet = "../../../data/2W_UTF8.csv"
    print("loading data....", dataSet, file=f)
    data = pd.read_csv(dataSet)
    print(data.info(),file=f)
    print("size of dataset :", data.size, file=f)
    print("shape of dataset :", data.shape, file=f)
    print("length of data set :", len(data),file=f)
    print(data.columns,file=f)

    G = nx.DiGraph()
    for i in range(len(data)):
        loaner_name = data.get_value(i, 'loaner_name')
        tender_name = data.get_value(i, 'tender_name')
        G.add_node(tender_name,node_color='r')
        G.add_node(loaner_name,node_color='g')
        G.add_weighted_edges_from([(tender_name, loaner_name, 1.0)])
    
    out_users = []