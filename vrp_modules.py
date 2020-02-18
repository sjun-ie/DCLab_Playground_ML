import math
import matplotlib.pyplot as plot
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import copy


class VRP_Info:
    def __init__(self):
        self.type = 'VRP'
        self.return_depot = False
        self.objective = 'Total_Distance'
        self.dist_func = get_distance_euc
        self.depot = Task()


class Vehicle_Info:  # define basic information of vehicle
    def __init__(self):
        self.id = 0
        self.loc = []
        self.max_capacity = 0
        self.avail_time = 0  # in hours
        self.speed = 40  # in km/h
        self.origin = []


class Task_Info:  # define basic information of task to be done
    def __init__(self):
        self.id = 0
        self.type = 'NA'
        self.loc = []
        self.srv_time = 0
        self.paired_ID = -1
        self.payload = -1
        self.tw_e = 0
        self.tw_l = 0

    def find_pair(self, tasklist):
        if self.paired_ID == -1:
            Exception('Cannot Find the Paired Tasks')
        try:
            paired_task = filter(lambda x: x.id == self.paired_ID, tasklist)
        except Exception:
            raise Exception('Cannot Find the Paired Tasks')
        return paired_task[0]


class Vehicle(Vehicle_Info):
    def __init__(self):
        Vehicle_Info.__init__(self)
        self.now_capacity = 0
        self.priority = -1
        self.cum_distance = 0
        self.cum_lateness = 0
        self.cum_tardiness = 0
        self.servedID = []
        self.can_serve = True

    def serve(self, target, dist_callback):
        if not self.doable(target): raise Exception('Infeasible Serving!')
        target.done = True
        req_distance = dist_callback(self.loc, target.loc)
        self.cum_distance += req_distance
        self.avail_time += req_distance / self.speed
        self.avail_time = max(self.avail_time, target.tw_e)
        if target.id != 0:
            self.cum_tardiness += max(0, self.avail_time - target.tw_l)
        self.avail_time += target.srv_time
        self.loc = target.loc
        self.servedID.append(target.id)
        self.now_capacity += target.payload
        if target.id != 0:
            self.cum_lateness += self.avail_time
        return target

    def doable(self, target):
        if target.id != 0 and target.done:
            return False
        if self.max_capacity < (self.now_capacity + target.payload):
            return False
        if (target.type == 'D') and (target.paired_ID in self.servedID):  # Previous Picked Up by 'vehicle'
            return True
        elif target.type == 'D' and (target.paired_ID not in self.servedID):  # Previous Picked Up by 'vehicle'
            return False
        else:  # Pickup
            return True


class Task(Task_Info):
    def __init__(self):
        Task_Info.__init__(self)
        self.done = False
        self.priority = -1
        self.picked = False


class prob_instance():
    def __init__(self):
        self.prob = None
        self.tasklist = None
        self.vhclist = None

    def deepcopy(self):
        return copy.deepcopy(self)


def get_distance_lat(coord1, coord2):
    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))  # Returns in meters


def get_distance_euc(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_distance_ret(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    return abs(x1 - x2) + abs(y1 - y2)


def plot_schedule(solution, add_label=False, arrow_size=10):
    (prob, vhclist, tasklist) = (solution['Problem'], solution['Vehicles'], solution['Tasks'])
    np.random.seed(101)
    values = range(len(vhclist))
    jet = cm = plot.get_cmap('jet')
    cNorm = colors.Normalize(vmin=0, vmax=values[-1])
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

    p_points = []
    d_points = []
    for task in tasklist:
        if task.type == 'P':
            p_points.append((task.loc[0], task.loc[1]))
            if add_label:
                plot.text(task.loc[0] - 10, task.loc[1] - 10, str(task.id) + '(P)', fontsize=8, alpha=0.8)
        else:
            d_points.append((task.loc[0], task.loc[1]))
            if add_label:
                plot.text(task.loc[0] - 10, task.loc[1] - 10, str(task.id) + '(D)', fontsize=8, alpha=0.8)

    plot.scatter(prob.depot.loc[0], prob.depot.loc[1], marker='s', color='blue', alpha=0.7)
    plot.scatter(list(map(lambda x: x[0], p_points)), list(map(lambda x: x[1], p_points)), marker='^', color='red',
                 alpha=0.7)
    plot.scatter(list(map(lambda x: x[0], d_points)), list(map(lambda x: x[1], d_points)), marker='v', color='green',
                 alpha=0.7)

    for vhc in vhclist:
        rng = np.random.RandomState(0)
        colorVal = scalarMap.to_rgba(values[vhc.id - 1])
        colorText = ('Vehicle ' + str(vhc.id))
        nowloc = vhc.origin
        for id in vhc.servedID:
            if not id == 0:
                nextone = next((task for task in tasklist if task.id == id), None)
                if nextone.loc != nowloc:
                    plot.arrow(nowloc[0], nowloc[1], nextone.loc[0] - nowloc[0], nextone.loc[1] - nowloc[1],
                               length_includes_head=True, color=colorVal, label=colorText, head_width=arrow_size,
                               head_length=arrow_size,
                               alpha=0.5)
                nowloc = nextone.loc
            else:
                plot.arrow(nowloc[0], nowloc[1], prob.depot.loc[0] - nowloc[0], prob.depot.loc[1] - nowloc[1],
                           length_includes_head=True, color=colorVal, label=colorText, head_width=arrow_size, head_length=arrow_size,
                           alpha=0.5)
    plot.show()


def check_feasiblity(solution):
    (prob, vhclist, tasklist) = (solution['Problem'], solution['Vehicles'], solution['Tasks'])
    error = ''
    for task in tasklist:
        if not task.done:
            error += 'No Allocation of Task ' + task.id + ', '
        if task.type == 'P':
            pair = [task.id, task.paired_ID]
            exists = False
            for vhc in vhclist:
                if all(elem in vhc.servedID for elem in pair): exists = True
            if not exists:
                error += 'No Allocation of Pairs ' + task.id + ', '

    served_count = 0
    for vhc in vhclist:
        served_count += len(vhc.servedID) - 1

    if served_count != len(tasklist):
        error += 'Missing tasks in Vehicles. '

    return error
