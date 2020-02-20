# import all the libraries required
import time
import os
import psutil

# initialize variables to be used as global
n = 0
p = 0
save = 0


def check_goal(in_list):                         # check if the list passed is the goal or not, and return accordingly
    if in_list == goal:
        return True
    return False


# check if the state has been visited before by comparing current list with visited list
def check_if_visited(check_list, p, c):
    global n
    global save
    if check_list in visited:
        pass
    else:
        queue.append(check_list)
        n += 1
        bfs_dict[n] = [p, c]
        # if state is new, append the parent node number p and move character c to the bfs_dictionary
        if check_goal(check_list):
            save = n


def left(l_list, i, p):
    if i in {0, 4, 8, 12}:                                      # if 0 is in the extreme left, skip left operation
        pass
    else:
        l_list[i - 1], l_list[i] = l_list[i], l_list[i - 1]     # Exchange 0 with its left neighbour
        check_if_visited(l_list[:], p, c='L')


def right(r_list, i, p):
    if i in {3, 7, 11, 15}:                                     # if 0 is in the extreme right, skip right operation
        pass
    else:
        r_list[i + 1], r_list[i] = r_list[i], r_list[i + 1]     # Exchange 0 with its right neighbour
        check_if_visited(r_list[:], p, c='R')


def up(u_list, i, p):
    if i in {0, 1, 2, 3}:                                       # if 0 is in the extreme top, skip up operation
        pass
    else:
        u_list[i - 4], u_list[i] = u_list[i], u_list[i - 4]     # Exchange 0 with its upper neighbour
        check_if_visited(u_list[:], p, c='U')


def down(d_list, i, p):
    if i in {12, 13, 14, 15}:                                   # if 0 is in the extreme bottom, skip down operation
        pass
    else:
        d_list[i + 4], d_list[i] = d_list[i], d_list[i + 4]     # Exchange 0 with its lower neighbour
        check_if_visited(d_list[:], p, c='D')


def bfs():                                                      # main function
    global p
    bfs_dict[0] = [None, '']
    queue.append(m_list)
    while len(queue) > 0:                                       # check if queue is empty
        visited.append(queue[0])                                # append the first list in queue to the visited list
        if check_goal(queue[0]):                                # check if goal is found and print output accordingly
            print("Goal state found!")
            move = [bfs_dict[save][1]]
            f = bfs_dict[save][0]
            while bfs_dict[f][0] is not None:
                move.append(bfs_dict[f][1])
                f = bfs_dict[f][0]
            moves = ''.join(move[::-1])
            print("Moves:", moves)
            print("Number of Nodes expanded:", len(visited))
            end = time.time()
            print("Time Taken:", end - start, "seconds")        # if time > 0.1 s
            process = psutil.Process(os.getpid())
            print("Memory Used:", process.memory_info().rss / 1000, "kb")
            break
        else:
            i = queue[0].index(0)                               # find index of the location of 0
            left(queue[0][:], i, p)                             # perform left-shift operation
            right(queue[0][:], i, p)                            # perform right-shift operation
            up(queue[0][:], i, p)                               # perform top-shift operation
            down(queue[0][:], i, p)                             # perform bottom-shift operation
            p += 1
            queue.pop(0)
            mid = time.time()
            if (mid - start) > 30.0:                            # stop if the bfs takes more than 30 seconds
                print("Solution not found")
                return


ip = input("Enter input state: ")                              # get the input
m_list = list(map(int, ip.split()))                            # convert to int and put into a list
start = time.time()                                            # start process timer after the input has been taken
visited = []
queue = []
bfs_dict = {}
goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]  # goal state
bfs()
