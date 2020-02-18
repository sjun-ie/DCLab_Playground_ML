import pandas as pd
import vrp_modules as vrp
import math


def load_prob_xlsx(path):
    # Load Excel file as a class
    df_task = pd.read_excel(path, sheet_name='Tasks')
    df_vehicle = pd.read_excel(path, sheet_name='Vehicles')
    df_prob = pd.read_excel(path, sheet_name='Problem')

    # Getting problem Settings
    objective_row = df_prob.loc[df_prob['Parameters'] == 'Objective'].index.values
    returncond_row = df_prob.loc[df_prob['Parameters'] == 'Return to Depot?'].index.values
    type_row = df_prob.loc[df_prob['Parameters'] == 'Type'].index.values
    problem = vrp.VRP_Info()
    problem.objective = df_prob.loc[objective_row[0], 'Value']
    problem.type = df_prob.loc[type_row[0], 'Value']
    if df_prob.loc[returncond_row[0], 'Value'] == 'Yes':
        problem.return_depot = True
        problem.depot.loc = [df_prob.loc[returncond_row[0], 'Param1'], df_prob.loc[returncond_row[0], 'Param2']]
    else:
        problem.return_depot = False
    problem.dist_func = vrp.get_distance_ret

    tasks = []
    for index, row in df_task.iterrows():
        this_task = vrp.Task()
        this_task.id = int(row['ID'])
        this_task.loc = [row['Pos1'], row['Pos2']]
        this_task.srv_time = row['Stime']
        this_task.payload = row['Payload']
        this_task.type = row['Type']
        if problem.type == 'PDP' and this_task.type == 'D':
            this_task.payload = - this_task.payload
        this_task.paired_ID = int(row['Pair'])
        this_task.tw_e = row['E']
        this_task.tw_l = row['L']
        tasks.append(this_task)

    vehicles = []
    for index, row in df_vehicle.iterrows():
        this_vhc = vrp.Vehicle()
        this_vhc.id = int(row['ID'])
        this_vhc.loc = [row['Pos1'], row['Pos2']]
        this_vhc.max_capacity = row['Capacity']
        this_vhc.speed = row['Speed']
        this_vhc.origin = this_vhc.loc
        vehicles.append(this_vhc)

    this_instance = vrp.prob_instance()
    this_instance.prob = problem
    this_instance.tasklist = tasks
    this_instance.vhclist = vehicles

    return this_instance


def get_google_data(this_instance):
    (tasks, vehicles, problem) = (this_instance.tasklist, this_instance.vhclist, this_instance.prob)
    g_data = {}
    p_d_pair = []
    for p_task in tasks:
        if p_task.type == 'P':
            p_d_pair.append([p_task.id, p_task.paired_ID])
    g_data['pickups_deliveries'] = p_d_pair
    g_data['num_vehicles'] = len(vehicles)
    g_data['depot'] = 0
    dist_mat = []
    for id in range(0, len(tasks) + 1):
        if id == 0:
            dist = []
            for id2 in range(0, len(tasks) + 1):
                if id == id2:
                    dist.append(0)
                else:
                    id2_task = next(x for x in tasks if x.id == id2)
                    dist.append(int(problem.dist_func(problem.depot.loc, id2_task.loc)))
            dist_mat.append(dist)
        else:
            dist = []
            for id2 in range(0, len(tasks) + 1):
                if id2 == 0:
                    id_task = next(x for x in tasks if x.id == id)
                    dist.append(int(problem.dist_func(id_task.loc, problem.depot.loc)))
                else:
                    id_task = next(x for x in tasks if x.id == id)
                    id2_task = next(x for x in tasks if x.id == id2)
                    dist.append(int(problem.dist_func(id_task.loc, id2_task.loc)))
            dist_mat.append(dist)
    g_data['distance_matrix'] = dist_mat
    return g_data


def load_prob_txt(path):
    problem = vrp.VRP_Info()
    problem.objective = 'Total_Distance'
    problem.type = 'PDP'
    problem.return_depot = True
    problem.dist_func = vrp.get_distance_euc

    def read_elem(filename):
        with open(filename) as f:
            return [str(elem) for elem in f.read().split()]

    def compute_distance_matrix(customers_x, customers_y):
        nb_customers = len(customers_x)
        distance_matrix = [[None for i in range(nb_customers)] for j in range(nb_customers)]
        for i in range(nb_customers):
            distance_matrix[i][i] = 0
            for j in range(nb_customers):
                dist = problem.dist_func([customers_x[i], customers_y[i]], [customers_x[j], customers_y[j]])
                distance_matrix[i][j] = dist
                distance_matrix[j][i] = dist
        return distance_matrix

    def compute_distance_warehouses(depot_x, depot_y, customers_x, customers_y):
        nb_customers = len(customers_x)
        distance_warehouses = [None for i in range(nb_customers)]
        for i in range(nb_customers):
            dist = problem.dist_func([depot_x, depot_y], [customers_x[i], customers_y[i]])
            distance_warehouses[i] = dist
        return distance_warehouses

    file_it = iter(read_elem(path))

    nb_trucks = int(next(file_it))
    truck_capacity = int(next(file_it))
    speed = int(next(file_it))

    next(file_it)

    warehouse_x = int(next(file_it))
    warehouse_y = int(next(file_it))

    for i in range(2): next(file_it)

    max_horizon = int(next(file_it))

    for i in range(3): next(file_it)

    customers_x = []
    customers_y = []
    demands = []
    earliest_start = []
    latest_end = []
    service_time = []
    pickUpIndex = []
    deliveryIndex = []

    while (1):
        val = next(file_it, None)
        if (val is None): break
        i = int(val) - 1
        customers_x.append(int(next(file_it)))
        customers_y.append(int(next(file_it)))
        demands.append(int(next(file_it)))
        ready = int(next(file_it))
        due = int(next(file_it))
        stime = int(next(file_it))
        pick = int(next(file_it))
        delivery = int(next(file_it))
        earliest_start.append(ready)
        latest_end.append(due)
        service_time.append(stime)
        pickUpIndex.append(pick - 1)
        deliveryIndex.append(delivery - 1)

    nb_customers = i + 1

    distance_matrix = compute_distance_matrix(customers_x, customers_y)
    distance_warehouses = compute_distance_warehouses(warehouse_x, warehouse_y, customers_x, customers_y)

    problem.depot.loc = [warehouse_x, warehouse_y]

    vehicles = []
    for vhc in range(0, nb_trucks):
        this_vhc = vrp.Vehicle()
        this_vhc.id = vhc + 1
        this_vhc.loc = [warehouse_x, warehouse_y]
        this_vhc.max_capacity = truck_capacity
        this_vhc.speed = speed
        this_vhc.origin = this_vhc.loc
        vehicles.append(this_vhc)

    tasks = []
    for task in range(0, nb_customers):
        pickid = pickUpIndex[task] + 1
        delid = deliveryIndex[task] + 1
        this_task = vrp.Task()
        this_task.id = task + 1
        this_task.loc = [customers_x[task], customers_y[task]]
        this_task.srv_time = service_time[task]
        this_task.payload = demands[task]
        if pickUpIndex[task] + 1 != 0:
            this_task.type = 'D'
            this_task.payload = demands[task]
            this_task.paired_ID = pickid
        else:
            this_task.type = 'P'
            this_task.payload = demands[task]
            this_task.paired_ID = delid
        this_task.tw_e = earliest_start[task]
        this_task.tw_l = latest_end[task]
        tasks.append(this_task)

    this_instance = vrp.prob_instance()
    this_instance.prob = problem
    this_instance.tasklist = tasks
    this_instance.vhclist = vehicles

    return this_instance

