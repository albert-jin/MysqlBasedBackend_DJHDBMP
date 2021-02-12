all_tables_info = {
    'activity_details':
        {'cols_info': {'id': 'INT UNSIGNED NOT NULL',
                       'title': 'CHAR(64) NOT NULL',
                       'publisher_type': 'CHAR(64) NOT NULL',
                       'start_time': 'DATETIME NOT NULL',
                       'end_time': 'DATETIME NOT NULL',
                       'deadline': 'DATETIME NOT NULL',
                       'content': 'VARCHAR(512) NOT NULL',
                       'status': 'BOOLEAN NOT NULL',
                       'pictures': 'VARCHAR(256) DEFAULT NULL',
                       'auditing_name': 'CHAR(64) NOT NULL',
                       'auditing_date': 'DATETIME NOT NULL',
                       'point_participant': 'FLOAT DEFAULT NULL',
                       'point_organizer': 'FLOAT DEFAULT NULL',
                       'pointer_others': 'FLOAT DEFAULT NULL'},
         'primary_key': ['id'],
         'foreign_key': {}
         },
    'member_user':
        {'cols_info': {'user_id': 'INT UNSIGNED NOT NULL',
                       'user_name': 'VARCHAR(64) NOT NULL',
                       'last_login_time': 'DATETIME NOT NULL',
                       'password': 'VARCHAR(32) NOT NULL',
                       'gender_isBoy': 'BOOLEAN NOT NULL',
                       'is_active': 'BOOLEAN NOT NULL',
                       'is_superuser': 'BOOLEAN NOT NULL'
                       },
         'primary_key': ['user_id'],
         'foreign_key': {}
    },
    'activity_student':
        {'cols_info': {'id': 'INT UNSIGNED NOT NULL',
                       'user_id': 'INT UNSIGNED NOT NULL',
                       'role':'VARCHAR(8) NOT NULL'
                       },
         'primary_key': ['id','user_id'],
         'foreign_key': {'user_id':'member_user(user_id)',
                         'id':'activity_details(id)'}
    }
}
