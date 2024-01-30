import pulp as op
import itertools as it

def model(N, p, s):
    m = op.LpProblem("SingleMachineSchedulingWithSequenceDependentSetuptime", op.LpMinimize)
    x = {(i, j): op.LpVariable(f"x{i}{j}", 0, 1, op.LpBinary) for i, j in it.product(range(N), range(N))}
    u = {i: op.LpVariable(f"u{i}", 0, None, op.LpInteger) for i in range(1, N)}
    objs = {0: sum((p[i] + s[f"order_{i}"][f"order_{j}"]) * x[(i, j)] for i in range(N) for j in range(N) if j != i)}
    cons = {0: {j: (sum(x[(i, j)] for i in range(N) if i != j) == 1, f"eq1_{j}") for j in range(N)},
            1: {i: (sum(x[(i, j)] for j in range(N) if j != i) == 1, f"eq2_{i}") for i in range(N)},
            2: {(i, j): (u[i] - u[j] + (N - 1) * x[(i, j)] <= N - 2, f"eq3_{i}{j}") for i in range(1, N) for j in
                range(1, N) if j != i},
            3: {i: (u[i] >= 1, f"eq4_{i}") for i in range(1, N)},
            4: {i: (u[i] <= N - 1, f"eq5_{i}") for i in range(1, N)},
            }
    m += objs[0]
    M = 1000  # BigM constraint
    # Here we need the number of weights according to the number of jobs, instad an error will occur  
    w = []  
    for job in range(0,N):
        w.append(1.0) 
    #w = [0.125, 0.125, 0.125, 0.125]
    J = range(len(p))
    K = range(len(J))
    y = {k: op.LpVariable(f"y{k}", 0, None, op.LpContinuous) for k in K}
    C = {j: op.LpVariable(f"C{j}", 0, None, op.LpContinuous) for j in J}
    u = {(j, k): op.LpVariable(f"u{j}{k}", 0, 1, op.LpBinary) for j, k in it.product(J, K)}  # (4.6
    objs = {0: sum(w[k] * y[k] for k in K)}
    cons = {0: {j: (sum(u[(j, k)] for k in K) == 1, f"eq1_{j}") for j in J},  # (4.1)
            1: {k: (sum(u[(j, k)] for j in J) == 1, f"eq2_{k}") for k in K},  # (4.2)
            2: {0: (y[0] >= sum(p[j] * u[(j, 0)] for j in J), "eq3_")},  # (4.3)
            3: {k: (y[k] >= y[k - 1] + sum(p[j] * u[(j, k)] for j in J), f"eq4_{k}") for k in K if k != 0},  # (4.4)
            4: {k: (y[k] >= 0, f"eq5_{k}") for k in K},  # (4.5)
            5: {(j, k): (C[j] >= y[k] - M * (1 - u[(j, k)]), f"eq6_{j}{k}") for k in K for j in J},  # (4.10)
            6: {j: (C[j] >= 0, f"eq7_{j}") for j in J}  # (4.11)
            }
    m += objs[0]
    for keys1 in cons:
        for keys2 in cons[keys1]: m += cons[keys1][keys2]
    return m, x, u, cons