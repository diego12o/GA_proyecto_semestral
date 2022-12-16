import networkx as nx
import courses_list
import adjacency_matrix
import algorithm
import functions
import time as t

def main():

    inicio = t.time()

    result = False
    while(not result):
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

        # GRAPH DAY CREATION
        graph_day = nx.Graph()
        graph_day.add_nodes_from(courses)

        for i in range(len(ad_matrix_day)-1):
            for j in range(i+1, len(ad_matrix_day)):
                if ad_matrix_day[i][j] == 1:
                    graph_day.add_edge(i, j)
        # APPLY GREEDY COLORING ALGORITHM
        algorithm.greedy_coloring_algorithm(graph_hor)
        algorithm.greedy_coloring_algorithm(graph_day)
                
        # GET NODES COLOR FOR DAYS
        dict_day = {}
        for v, data in graph_day.nodes(data=True):
            if data['color'] not in dict_day.keys():
                dict_day[data['color']] = []
            dict_day[data['color']].append(v)

        # GET NODES COLOR FOR HOR
        dict_hor = {}
        for v, data in graph_hor.nodes(data=True):
            dict_hor[v] = data['color']

        # EXAM SCHEDULING
        calendar, result = functions.exam_scheduling(dict_day, dict_hor)

    fin = t.time()

    for day in range(5):
        print("----------- DÍA " + str(day) + " -----------")
        for time in range(4):
            print("-- HORARIO " + str(time) + " --")
            for node in calendar[day][time]:
                print(str(node) + " " + dict_hor[node])

    print("TIEMPO: " + str(fin-inicio))

if __name__ == "__main__":
    main()