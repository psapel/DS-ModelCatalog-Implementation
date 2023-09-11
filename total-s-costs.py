import pulp as op
import itertools as it
import numberToJobName

s = {"order_0":{"order_0":0,"order_1":0,"order_2":0,"order_3":0,"order_4":0},
     "order_1":{"order_0":0,"order_1":0,"order_2":2,"order_3":5,"order_4":3},
     "order_2":{"order_0":0,"order_1":2,"order_2":0,"order_3":3,"order_4":2},
     "order_3":{"order_0":0,"order_1":6,"order_2":4,"order_3":0,"order_4":1},
     "order_4":{"order_0":0,"order_1":1,"order_2":3,"order_3":2,"order_4":0}}

p = [0,  90,   30,    70,    40] #Processing time of each job
job_names = ["WH00","WH6","WH010","WH13","WH16"]
N = len(p) # Set of jobs
dispmodel="y"
solve="y"
dispresult="y"

m = op.LpProblem("SingleMachineSchedulingWithSequenceDependentSetuptime", op.LpMinimize)
x = {(i,j): op.LpVariable(f"x{i}{j}", 0,1, op.LpBinary) for i,j in it.product(range(N),range(N))} 
u = {i: op.LpVariable(f"u{i}", 0, None, op.LpInteger) for i in range(1,N)} 

# Source: https://en.wikipedia.org/wiki/Travelling_salesman_problem
objs = {0: sum((p[i]+s[f"order_{i}"][f"order_{j}"])*x[(i,j)] for i in range(N) for j in range(N) if j!=i)} 
cons = {0: {j: (sum(x[(i,j)] for i in range(N) if i !=j) == 1, f"eq1_{j}") for j in range(N)}, # Constraint (1)
        1: {i: (sum(x[(i,j)] for j in range(N) if j!=i) == 1, f"eq2_{i}") for i in range(N)}, # Constraint (2)
        2: {(i,j): (u[i]-u[j]+(N-1)*x[(i,j)]<=N-2, f"eq3_{i}{j}") for i in range(1,N) for j in range(1,N) if j!=i}, # Constraint(3)
        3: {i: (u[i]>=1, f"eq4_{i}") for i in range(1,N)}, #Constraint (4)
        4: {i: (u[i]<=N-1, f"eq5_{i}") for i in range(1,N)}, #Constraint (4)
        }

m += objs[0]
for keys1 in cons: 
    for keys2 in cons[keys1]: m += cons[keys1][keys2]
    if dispmodel=="y":
        print("Model --- \n",m)
    if solve == "y":
        result = m.solve(op.PULP_CBC_CMD(timeLimit=None))
        print("Status --- \n", op.LpStatus[result])
        if dispresult == "y" and op.LpStatus[result] =='Optimal':
            #print("Objective --- \n", op.value(m.objective))
            result = [[variables.name,variables.varValue] for variables in m.variables() if variables.varValue!=0]
            #print("Decision --- \n", [[variables.name,variables.varValue] for variables in m.variables() if variables.varValue!=0])
[(i, j) for i in range(N) for j in range(N) if op.value(x[i, j]) == 1]


job_dict = numberToJobName.numberToJobName(result,job_names)


print("The optimal job order is: ",job_dict)