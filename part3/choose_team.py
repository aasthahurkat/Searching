#!/usr/local/bin/python3
#
# choose_team.py : Choose a team of maximum skill under a fixed budget
#
# Code by: [Rohit Rokde-rrokde, Bhumika Agrawal-bagrawal, Aastha Hurkat-aahurkat]
#
# Based on skeleton code by D. Crandall, September 2019
#
import sys
import copy

def load_people(filename):
    people={} #Used a dictionary for faster access of person data.
    with open(filename, "r") as file:
        for line in file:
            l = line.split()
            people[l[0]] = [ float(i) for i in l[1:] ]
    return people

def successors(args):

    possible_list = args[0]
    skill_sum = args[1]
    remaining_budget = args[2]

    if(remaining_budget <= 0):
        #The second value '-1' which is the skill, is used as a marker to select the right if statement in solve()
        return [("", -1, 0, copy.deepcopy(possible_list), skill_sum, remaining_budget)]
    hashtable = {()} #Hash table to check which robots were already added in the list
    if(len(possible_list) < len(people_sorted)):
        for (robot, skill, cost) in possible_list: #robot is same as person variable
            hashtable.add(robot)
            skill+cost  #USed this dummy code to remove compiler lint warning

        returnList = []
        update = False
        for (person, (skill, cost)) in people_sorted:
            if(person not in hashtable):
                if((remaining_budget-cost >= 0)):
                    update = True
                    returnList.append((person, skill, cost, copy.deepcopy(possible_list), skill_sum+skill, remaining_budget-cost))
            else:
                pass

        if(not update):
            #The second value '-2' which is the skill, is used as a marker to select the right if statement in solve()
            return [("", -2, 0, copy.deepcopy(possible_list), skill_sum, remaining_budget)]#Another solution
        else:
            return returnList
    else:
        return [("", 0, 0, copy.deepcopy(possible_list), skill_sum, remaining_budget)]#It means all the persons were added and no person is left

#Need this global variable to access the sorted list in successor
people_sorted = []
visited = {}
# This function implements a branch and bound solution to the problem:
#
def solve(people, budget):

    solution = []
    for itemm in sorted(people.items(), key=lambda x: x[1][1]):
        people_sorted.append(itemm)

    endpoint = False
    possible_list = []
    fringe = [ (possible_list, 0, budget) ]

    while len(fringe) > 0 and not endpoint:
        elem = fringe.pop()
        for (robot, skill, cost, possible_list, skill_sum, budget_for_this_selection) in successors(elem):
            if(skill == -1):#This condition will be selected when the budget is exhausted for the current selection
                key_gen = ""
                possible_list_temp = sorted(possible_list, key=lambda x: x[0])
                for i in possible_list_temp:
                    key_gen += i[0] + " "
                #print("key_gen", key_gen)
                if key_gen not in visited:
                    visited[key_gen] = key_gen
                solution.append( (possible_list, skill_sum, budget_for_this_selection))
                continue
            if(skill == -2):#This condition will be invoked when all the persons in the poeple list are selected.
                key_gen = ""
                possible_list_temp = sorted(possible_list, key=lambda x: x[0])
                for i in possible_list_temp:
                    key_gen += i[0] + " "
                #print("key_gen", key_gen)
                if key_gen not in visited:
                    visited[key_gen] = key_gen
                solution.append( (possible_list, skill_sum, budget_for_this_selection))
                continue
            if(skill == 0 and cost == 0):
                key_gen = ""
                possible_list_temp = sorted(possible_list, key=lambda x: x[0])
                for i in possible_list_temp:
                    key_gen += i[0] + " "
                #print("key_gen", key_gen)
                if key_gen not in visited:
                    visited[key_gen] = key_gen
                solution.append( (possible_list, skill_sum, budget_for_this_selection) )
                endpoint = True
                break

            possible_list.append((robot, skill, cost))
            key_gen = ""
            possible_list_temp = sorted(possible_list, key=lambda x: x[0])
            for i in possible_list_temp:
                key_gen += i[0] + " "
            #print("key_gen", key_gen)
            #print(possible_list_temp)
            if key_gen not in visited:
                visited[key_gen] = key_gen
                fringe.append( (possible_list, skill_sum, budget_for_this_selection) )

            if(len(possible_list) >= len(people_sorted)):
                solution.append((possible_list, skill_sum, budget_for_this_selection))
                endpoint = True #If the list reaches the end point, it means we have taken all the persons, and the budget could accomodate that

    #Sort according to skill and return the first element.
    sorted_solution = sorted([t for t in solution], key=lambda x: x[1], reverse=True)
    #for pp in sorted_solution:
    #    print(pp)
    if(len(sorted_solution) > 0):
        return sorted_solution[0]
    else:
        return [0]


if __name__ == "__main__":

    if(len(sys.argv) != 3):
        raise Exception('Error: expected 2 command line arguments')

    budget = float(sys.argv[2])
    people = load_people(sys.argv[1])

    solution = solve(people, budget)

    print("Found a group with %d people costing %f with total skill %f" % \
              ( len(solution[0]), budget-solution[2], solution[1]))

    for person in solution[0]:
        print(person[0], " 1.000000")#The exact format as per Assignment 1 instructions
