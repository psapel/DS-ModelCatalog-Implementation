import pulp as op

def process_result(result, m, job_names):
    result_temp = "Model name -- " + m.name + "\n\n"
    result_temp += "Status of solution -- " + op.LpStatus[result] + "\n\n"
    result_temp += "Objective -- " + str(op.value(m.objective)) + "\n\n"
    result_temp += "Decision -- " + str(
        [(variables.name, variables.varValue) for variables in m.variables() if variables.varValue != 0]) + "\n\n"

    seq = []
    for k in K:
        for j in J:
            if u[(j, k)].varValue == 1:
                seq.append(j + 1)

    job_dict = []
    for item in seq:
        indv_job = []
        indv_job.append("u" + str(item))
        indv_job.append(job_names[item - 1])
        job_dict.append(indv_job)

    result_temp += "Optimal Job Order: " + str(job_dict)
    return result_temp
