def exam_scheduling(dict_day, dict_hor):
    # CALENDAR CREATION
    calendar = [
        [ [], [], [], [] ],
        [ [], [], [], [] ],
        [ [], [], [], [] ],
        [ [], [], [], [] ],
        [ [], [], [], [] ]
    ]

    wait_list = []

    day = 0
    for key in dict_day.keys():
        calendar.append("día 1")
        time = 0
        colors = []
        for node in dict_day[key]:
            for time in range(4):
                if len(calendar[day][time])==0:
                    calendar[day][time].append(node)
                    break
                elif dict_hor[node] == dict_hor[calendar[day][time][0]]:
                    calendar[day][time].append(node)
                    break
                if time == 3:
                    wait_list.append(node)
        day = day + 1

    # for node in wait_list:
    #     for time in range(4):
    #             print(str(node) + " " + dict_hor[node])
    #             if len(calendar[day][time])==0:
    #                 calendar[day][time].append(node)
    #                 break
    #             elif dict_hor[node] == dict_hor[calendar[day][time][0]]:
    #                 calendar[day][time].append(node)
    #                 break

    if len(wait_list) > 0:
        print("Buscando solución...")
        return [], False
    
    return calendar, True