# This function builds a dict where iterative int-numbers were assigned to the given jobnames. Suitable for optimization with python bib pulp.

#job_names = ["WH00","WH6","WH010","WH13","WH16"]

def numberToJobName(result,job_names):
    # Building basic Dictionary where job-names were allocated to numbers
    job_dict = {}
    number_of_jobs = len(job_names)
    for key in range(len(job_names)):
        for value in job_names:
            job_dict[round(float(key),2)] = value
            job_names.remove(value)
            break 
    
    # Replace number from result-list with name
    for i in range(len(result)-number_of_jobs):
        result[i][1] = job_dict[result[i][1]]

    # Delete constraints prints, so only result is shown
    upper_bound = len(result)-1
    for i in range(number_of_jobs-1,upper_bound):
        result.pop(upper_bound)
        upper_bound-=1
        if number_of_jobs-1 == upper_bound:
            result.pop(upper_bound)
    return result