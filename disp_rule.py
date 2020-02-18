import vrp_modules as vrp


# Implementation of Dispatching Algorithms based on Vehicle-Initiated Dispatching Rule
def solve_dr_vi(_instance):
    local_copy = _instance.deepcopy()
    (prob, vhclist, tasklist) = (local_copy.prob, local_copy.vhclist, local_copy.tasklist)
    large_number = 1000000
    coeff_vhc = 0.1
    coeff_pickup = 0.5

    def update_tasklist(vehicle):
        for task in tasklist:
            if vehicle.doable(task):  # PDP Prioritization
                this_coeff = int(task.type == 'P') * coeff_pickup + int(task.type == 'D') * (1 - coeff_pickup)
                task.priority = this_coeff * prob.dist_func(task.loc, vehicle.loc)
            else:  # VRP Prioritization
                task.priority = large_number

    def update_vhclist():
        if not any(
                task.type == 'P' for task in filter(lambda x: x.done == False, tasklist)):  # only delivery tasks exit
            for vhc in vhclist:
                if any(vhc.doable(task) for task in filter(lambda x: x.done is False, tasklist)):
                    vhc.can_serve = True
                    vhc.priority = -1000
                else:
                    vhc.can_serve = False
        else:
            for vhc in vhclist:
                if any(vhc.doable(task) for task in tasklist):
                    vhc.can_serve = True
                    not_completed_tasks = list(filter(lambda x: x.done == False, tasklist))
                    avg_distance = sum(prob.dist_func(vhc.loc, task.loc) for task in not_completed_tasks) / len(
                        not_completed_tasks)
                    vhc.priority = vhc.avail_time + (avg_distance / vhc.speed) * coeff_vhc
                else:
                    vhc.can_serve = False

    solution = {}
    solution['status'] = 'Not Found'

    while any(task.done == False for task in tasklist):
        # Check whether there are available tasks for each vehicle
        update_vhclist()
        servable_vhcs = list(filter(lambda x: x.can_serve is True, vhclist))
        servable_vhcs.sort(key=lambda x: x.priority, reverse=False)
        try:
            next_vhc = servable_vhcs[0]
        except:
            raise Exception("Invalid Logic")
            break
        update_tasklist(next_vhc)
        tasklist.sort(key=lambda x: (x.done, x.priority), reverse=False)
        available_tasks = list(filter(lambda x: next_vhc.doable(x) and x.done is False, tasklist))
        try:
            next_vhc.serve(available_tasks[0], prob.dist_func)
        except Exception:
            raise Exception('Invalid Logic')
            break

    if prob.return_depot:
        for vhc in vhclist:
            vhc.serve(prob.depot, prob.dist_func)

    solution['status'] = 'Found'
    solution['Total_Distance'] = sum(vhc.cum_distance for vhc in vhclist)
    solution['Total_Lateness'] = sum(vhc.cum_lateness for vhc in vhclist)
    solution['Total_Tardiness'] = sum(vhc.cum_tardiness for vhc in vhclist)

    if prob.objective == 'Total_Distance':
        solution['objective'] = sum(vhc.cum_distance for vhc in vhclist)
    elif prob.objective == 'Total_Lateness':
        solution['objective'] = sum(vhc.cum_lateness for vhc in vhclist)
    elif prob.objective == 'Total_Tardiness':
        solution['objective'] = sum(vhc.cum_tardiness for vhc in vhclist)

    solution['Problem'] = prob
    solution['Vehicles'] = vhclist
    solution['Tasks'] = tasklist

    if not vrp.check_feasiblity(solution) == '':
        raise Exception('Infeasible Solution')

    return solution


# Implementation of Dispatching Algorithms based on Task-Initiated Dispatching Rule
def solve_dr_ti(_instance):
    local_copy = _instance.deepcopy()
    (prob, vhclist, tasklist) = (local_copy.prob, local_copy.vhclist, local_copy.tasklist)
    large_number = 1000000
    coeff_vhc = 0.01
    coeff_pickup = 0.35

    def update_tasklist():
        for task in tasklist:
            is_picked = any((ptask.picked is True and ptask.id == task.paired_ID) for ptask in tasklist)
            if task.type == 'D' and is_picked is False:
                task.priority = large_number
            elif task.done is True:
                task.priority = large_number
            else:
                task.priority = task.tw_l

    def update_vhclist(target):
        for vhc in vhclist:
            if vhc.doable(target):
                vhc.can_serve = True
                vhc.priority = prob.dist_func(target.loc, vhc.loc)/vhc.speed + vhc.avail_time  # expected arrival time
            else:
                vhc.can_serve = False

    solution = {}
    solution['status'] = 'Not Found'

    while any(task.done is False for task in tasklist):
        # Check whether there are available tasks for each vehicle
        update_tasklist()
        not_completed_tasks = list(filter(lambda x: x.done is False, tasklist))
        not_completed_tasks.sort(key=lambda x: x.priority, reverse=False)

        update_vhclist(not_completed_tasks[0])
        servable_vhcs = list(filter(lambda x: x.can_serve is True, vhclist))
        servable_vhcs.sort(key=lambda x: x.priority, reverse=False)

        try:
            servable_vhcs[0].serve(not_completed_tasks[0], prob.dist_func)
        except Exception:
            raise Exception('Invalid Logic')
            break

    if prob.return_depot:
        for vhc in vhclist:
            vhc.serve(prob.depot, prob.dist_func)

    solution['status'] = 'Found'
    solution['Total_Distance'] = sum(vhc.cum_distance for vhc in vhclist)
    solution['Total_Lateness'] = sum(vhc.cum_lateness for vhc in vhclist)
    solution['Total_Tardiness'] = sum(vhc.cum_tardiness for vhc in vhclist)

    if prob.objective == 'Total_Distance':
        solution['objective'] = sum(vhc.cum_distance for vhc in vhclist)
    elif prob.objective == 'Total_Lateness':
        solution['objective'] = sum(vhc.cum_lateness for vhc in vhclist)
    elif prob.objective == 'Total_Tardiness':
        solution['objective'] = sum(vhc.cum_tardiness for vhc in vhclist)

    solution['Problem'] = prob
    solution['Vehicles'] = vhclist
    solution['Tasks'] = tasklist

    if not vrp.check_feasiblity(solution) == '':
        raise Exception('Infeasible Solution')

    return solution