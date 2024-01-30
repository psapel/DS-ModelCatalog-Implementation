import itertools as it

def preprocessing(model_name):
    
    response = model_name
    p = []  # Processing time of each job
    job_names = []
    for i in range(0, len(response)):
        current_job = response[i]['name']
        current_duration = response[i]['production_duration_expected']
        if current_job:
            job_names.append(current_job)
        if current_duration:
            p.append(current_duration)

    return p, job_names
