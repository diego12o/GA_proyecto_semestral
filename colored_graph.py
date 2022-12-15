import networkx as nx
import courses_list
import adjacency_matrix

# PARAMETER DEFINITION
courses = courses_list.courses
ad_matrix_hor = adjacency_matrix.ad_matrix_hor
ad_matrix_day = adjacency_matrix.ad_matrix_day

# GRAPH HOR CREATION
graph_hor = nx.Graph()
graph_hor.add_nodes_from(courses)

for i in range(len(ad_matrix_hor)-1):
    for j in range(i+1, len(ad_matrix_hor)):
        if ad_matrix_hor[i][j] == 1:
            graph_hor.add_edge(i, j)

