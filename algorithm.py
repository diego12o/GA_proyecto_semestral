import random

colors = [
    "lightcoral", "gray", "lightgray", "firebrick", "red", "chocolate", 
    "darkorange", "moccasin", "gold", "yellow", "darkolivegreen", "chartreuse", 
    "forestgreen", "lime", "mediumaquamarine", "turquoise", "teal", "cadetblue",
    "dogerblue", "blue", "slateblue", "blueviolet", "magenta", "lightsteelblue"
]

def greedy_coloring_algorithm(network):
    nodes = list(network.nodes()) 
    random.shuffle(nodes) # step 1 random ordering
    for node in nodes:
        dict_neighbors = dict(network[node])
# gives names of nodes that are neighbors
        nodes_neighbors = list(dict_neighbors.keys())
        
        forbidden_colors = []
        for neighbor in nodes_neighbors:
            if len(network.nodes.data()[neighbor].keys()) == 0: 
                # if the neighbor has no color, proceed
                continue
            else:
                # if the neighbor has a color,
                # this color is forbidden
                forbidden_color = network.nodes.data()[neighbor]
                forbidden_color = forbidden_color['color']
                forbidden_colors.append(forbidden_color)
        # assign the first color 
        # that is not forbidden
        for color in colors:
            # step 2: start everytime at the top of the colors,
            # so that the smallest number of colors is used
            if color in forbidden_colors:
                continue
            else:
                # step 3: color one node at the time
                network.nodes[node]['color'] = color
                break