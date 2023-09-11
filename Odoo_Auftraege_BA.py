"""
Created on Sat Nov 26 2022

@author: Patrick Sapel
"""
##### Administration #####

# imports
import xmlrpc.client
import json
import copy
from datetime import date

def odoo():
    # Odoo User
    user_ps = 'patrick.sapel@ikv.rwth-aachen.de'
    pw_ps = 'ikv123!'

    # Database credentials
    url = 'https://edu-ikvds-rwth-aachen.odoo.com'
    db = 'edu-ikvds-rwth-aachen'
    username = user_ps
    password = pw_ps

    # Establish odoo DB connection (with our without SSH)
    # xmlrpc/c/common: Ruft Daten ohne Authentifizierung auf
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    #common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url), context=ssl._create_unverified_context())
    #print(common.version())

    # Authentication with params
    uid = common.authenticate(db, username, password, {})
    #print(uid) #for checking

    # Initiating of models
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    #models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url),context=ssl._create_unverified_context())

    # ÜCheck if login was successful (boolean)
    
    #print(models.execute_kw(db, uid, password,
    #    'res.partner', 'check_access_rights',
    #    ['read'], {'raise_exception': False}))
    # documentation: https://www.odoo.com/documentation/15.0/developer/misc/api/odoo.html
    

    ###### Read odoo data #####

    # select relevant jobs by its status
    state = ['confirmed','progress'] # draft, confirmed, progress, to_close, done, cancel

    # Read jobs
    jobs = (models.execute_kw(db, uid, password,
        'mrp.production', 'search_read', 
        [[['state','=', state]]],
        {'fields': ['name','production_duration_expected','date_planned_finished']}))

    # Building a deepcopy to prohibit errors in original file
    jobs_copy = copy.deepcopy(jobs)

    # Definition of needed variables
    # name = name of job j
    # pj = Processing time of job j

    # Read names of jobs
    name_first = []  
    name_first_array = []
    i_name_ini = 0
    i_name_end = len(jobs_copy) - 1

    # Insert values for name
    while i_name_ini <= i_name_end:
        name_first = jobs_copy[i_name_ini]['name']
        name_first_array.append(name_first)
        i_name_ini = i_name_ini + 1

    # Read production_duration_expected from all jobs
    pj_first = []  
    pj_first_array = []
    i_pj_ini = 0
    i_pj_end = len(jobs_copy) - 1

    # Insert values for production_duration_expected
    while i_pj_ini <= i_pj_end:
        pj_first = jobs_copy[i_pj_ini]['production_duration_expected']
        pj_first_array.append(pj_first)
        i_pj_ini = i_pj_ini + 1

    # Read origin
    origin = []  
    origin_array = []
    i_origin_ini = 0
    i_origin_end = len(jobs_copy) - 1

    # Insert values for origin
    while i_origin_ini <= i_origin_end:
        origin = jobs_copy[i_origin_ini]['date_planned_finished']
        origin_array.append(origin)
        i_origin_ini = i_origin_ini + 1

    #actual date, because odoo date is not compatible to algorithm date
    actual_date = date.today()
    #print(actual_date)
    # Printing results
    """
    print("Number of jobs to be considered: " + str(len(jobs_copy)))
    i = 0
    i_end = len(jobs_copy) - 1
    while i <= i_end:
        print("job name: " + str(name_first_array[i]) + " | duration: " + str(pj_first_array[i]) + " | due date: " + str(origin_array[i]))
        i = i+1
    """
    return name_first_array, pj_first_array, origin_array

print(odoo())