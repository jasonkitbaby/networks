# -*- coding: utf-8 -*-

import networkx as nx
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from networkx.algorithms import bipartite



#
#  构建“用户----产品 二分网 



if __name__ == '__main__':
    
  
    f = open('../../../logs/part2-module2.logs','w')	
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
        loan_id = data.get_value(i, 'loanid')
        tender_name = data.get_value(i, 'tender_name')
        G.add_node(tender_name,node_color='r')
        G.add_node(loan_id,node_color='g')
        G.add_weighted_edges_from([(tender_name, loan_id, 1.0)])

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=False,node_size=0.5, width=0.1, edge_color='gray',node_color=('red','green'),dpi=1024, figsize=2048)
    plt.savefig("../../../target/用户-产品-有向图.png",dpi=1024,figsize=1024)
    # plt.show()

    print("graph info:", nx.info(G), file=f)
