all_tables_info={
'activity_details':
    {'cols_info':{'id':'INT UNSIGNED NOT NULL',
                  'title':'CHAR(64) NOT NULL',
                  'publisher_type':'CHAR(64) NOT NULL',
                  'start_time':'DATETIME NOT NULL',
                  'end_time':'DATETIME NOT NULL',
                  'deadline':'DATETIME NOT NULL',
                  'content':'VARCHAR(512) NOT NULL',
                  'status':'BOOLEAN NOT NULL',
                  'pictures':'VARCHAR(256) DEFAULT NULL',
                  'auditing_name':'CHAR(64) NOT NULL',
                  'auditing_date':'DATETIME NOT NULL',
                  'point_participant':'FLOAT DEFAULT NULL',
                  'point_organizer':'FLOAT DEFAULT NULL',
                  'pointer_others':'FLOAT DEFAULT NULL'},
    'primary_key':['id'],
    'foreign_key':{}
     }
}