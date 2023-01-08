li_ports = ["BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN", "JFK", "LGA",
"LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"]
li_con = [
["DSM", "ORD"],
["ORD", "BGI"],
["BGI", "LGA"],
["SIN", "CDG"],
["CDG", "SIN"],
["CDG", "BUD"],
["DEL", "DOH"],
["DEL", "CDG"],
["TLV", "DEL"],
["EWR", "HND"],
["HND", "ICN"],
["HND", "JFK"],
["ICN", "JFK"],
["JFK", "LGA"],
["EYW", "LHR"],
["LHR", "SFO"],
["SFO", "SAN"],
["SFO", "DSM"],
["SAN", "EYW"]
]
head = "LGA"

def pos(li, item):
    count = 0
    for i in li:
        if i == item:
            return count
        count += 1
    else:
        return None

def all_direct(li_con, center): # all direct connections from center to anywhere other than head
    li_direct = []
    for con in li_con:
        if con[0] == center and con[1] != head and con[1] not in li_direct:
            li_direct.append(con[1])
                
    return li_direct


def all_con_step(li_con, center, step): # ALL connections from center to anywhere other than head with given step
    if step == 1:
        return all_direct(li_con, center)
    else:
        li_penultimate = all_con_step(li_con, center, step-1)
        for i in li_penultimate:
            for j in all_direct(li_con, i):
                if j not in li_penultimate:
                    li_penultimate.append(j)
    return li_penultimate


def all_con(li_con, center):
    li = all_direct(li_con, center)
    step = 2
    done = False
    while done == False:
        if li == all_con_step(li_con, center, step):
            break
        else:
            li = all_con_step(li_con, center, step)
            step += 1
    return li

### Main code

def solve_one_step(li_ports, li_con, head):
    li_left = []
    li_all = all_con(li_con, head)
    li_all.append(head)
    
    for item in li_ports:
        if item not in li_all:
            li_left.append(item)
    
    if li_left == []:
        return None
       
    li_left_con = []
    max_score = 0
    max_score_pos = []
    for left in li_left:
        li_left_con.append(all_con(li_con, left))
        score = len(all_con(li_con, left))
        if score > max_score:
            max_score = score
            max_score_pos = pos(li_left, left)
    
    return li_left[max_score_pos]

def solve(li_ports, li_con, head):
    li_con_to_be_made = [] 
    done = False
    while done == False:
        connect_to = solve_one_step(li_ports, li_con, head)
        if connect_to == None:
            done = True
        else:
            li_con_to_be_made.append(connect_to)
            li_con.append([head, connect_to])
            
    return li_con_to_be_made


print(solve(li_ports, li_con, head))
