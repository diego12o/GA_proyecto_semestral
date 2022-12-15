import networkx as nx
import courses_list
import adjacency_matrix
import algorithm
import numpy as np

def main():
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

    # CALENDAR CREATION
    days = {}
    calendar = [
        [ [], [], [], [] ],
        [ [], [], [], [] ],
        [ [], [], [], [] ],
        [ [], [], [], [] ],
        [ [], [], [], [] ]
    ]
            
    # GET NODES COLOR FOR DAYS
    for v, data in graph_day.nodes(data=True):
        if data['color'] not in days.keys():
            days[data['color']] = []
        days[data['color']].append(v)

    # GET NODES COLOR FOR HOR
    dict_hor = {}
    for v, data in graph_hor.nodes(data=True):
        dict_hor[v] = data['color']

    # EXAM SCHEDULING
    wait_list = []
    day = 0
    for key in days.keys():
        calendar.append("día 1")
        time = 0
        colors = []
        for node in days[key]:
            for time in range(4):
                print(str(node) + " " + dict_hor[node])
                if len(calendar[day][time])==0:
                    calendar[day][time].append(node)
                    break
                elif dict_hor[node] == dict_hor[calendar[day][time][0]]:
                    calendar[day][time].append(node)
                    break
                elif time == 3:
                    wait_list.append(node)
        day = day + 1

    for node in wait_list:
        for time in range(4):
                print(str(node) + " " + dict_hor[node])
                if len(calendar[day][time])==0:
                    calendar[day][time].append(node)
                    break
                elif dict_hor[node] == dict_hor[calendar[day][time][0]]:
                    calendar[day][time].append(node)
                    break

    if len(wait_list) > 0:
        print("Sin solución")
        return False
    
    for day in range(5):
        print("----------- DÍA " + str(day) + " -----------")
        for time in range(4):
            print("-- HORARIO " + str(time) + " --")
            for node in calendar[day][time]:
                print(str(node) + " " + dict_hor[node])

            


if __name__ == "__main__":
    main()