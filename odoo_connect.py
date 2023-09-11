import xmlrpc.client
import json
import copy
from datetime import date

def connect():
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
    
    print(models.execute_kw(db, uid, password,
        'res.partner', 'check_access_rights',
        ['read'], {'raise_exception': False}))
    # documentation: https://www.odoo.com/documentation/15.0/developer/misc/api/odoo.html