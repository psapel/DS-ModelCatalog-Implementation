import pulp as op

def postprocessing(m, x, p, job_names, dispmodel, solve, dispresult):
    result_temp = ""

    if dispmodel == "y":
        result_temp += "Model --- \n" + str(m) + "\n"

    if solve == "y":
        result = m.solve(op.PULP_CBC_CMD(timeLimit=None))
        result_temp += "Status --- \n" + op.LpStatus[result] + "\n"

        if dispresult == "y" and op.LpStatus[result] == 'Optimal':
            result_temp += "Objective --- \n" + str(op.value(m.objective)) + "\n"
            
            seq = []
            for k in range(len(p)):
                for j in range(len(p)):
                    if x[(j, k)].varValue == 1:
                        seq.append(j + 1)

            print(seq)
            print(m.name)
            job_dict = []
            for item in seq:
                indv_job = []
                indv_job.append("u" + str(item))
                indv_job.append(job_names[item - 1])
                job_dict.append(indv_job)

            result_temp += "Decision --- \n" + str([(variables.name, variables.varValue) for variables in m.variables() if variables.varValue != 0]) + "\n"
            result_temp += "Optimal Job Order: " + str(job_dict) + "\n"

    result_temp += "List of Jobs : " + str(job_names) + "\n\n"
    result_temp += "Model name -- " + m.name + "\n\n"
    result_temp += "Status of solution -- " + op.LpStatus[result] + "\n\n"
    result_temp += "Objective -- " + str(op.value(m.objective)) + "\n\n"

    return result_temp, result