#!/usr/local/bin/python3
#
# choose_team.py : Choose a team of maximum skill under a fixed budget
#
# Code by: [Rohit Rokde-rrokde, Bhumika Agrawal-bagrawal, Aastha Hurkat-aahurkat]
#
# Based on skeleton code by D. Crandall, September 2019
#
import sys

def load_people(filename):
    people={}
    with open(filename, "r") as file:
        for line in file:
            l = line.split()
            people[l[0]] = [ float(i) for i in l[1:] ] + [0]
    return people


# This function implements a greedy solution to the problem:
#  It adds people in decreasing order of "skill per dollar,"
#  until the budget is exhausted.
#
def approx_solve(people, budget):

    solution=()
    print(people.items())
    ppl = sorted(people.items(), key=lambda x: x[1][0]/x[1][1])
    print("Sorted list = ")
    print(ppl)
    ppl.reverse()
    print("Reverse list = ")
    print(ppl)
    for (person, (skill, cost, count)) in ppl:
        print(person, (skill, cost, count))
        while(int(budget - cost) > 0):
            count+=1
            budget -= cost
        if int(count) != 0:
            solution += ( ( person, int(count)), )

    return solution


if __name__ == "__main__":

    if(len(sys.argv) != 3):
        raise Exception('Error: expected 2 command line arguments')

    budget = float(sys.argv[2])
    people = load_people(sys.argv[1])
    solution = approx_solve(people, budget)

    print("Found a group with %d people costing %f with total skill %f" % \
               ( len(solution), sum(people[p][1]*f for p,f in solution), sum(people[p][0]*f for p,f in solution)))

    for s in solution:
        print("%s %i" % s)

