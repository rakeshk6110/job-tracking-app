import sqlite3, os
path='db.sqlite3'
print('exists', os.path.exists(path))
con=sqlite3.connect(path)
cur=con.cursor()
for t in ['jobs_job','jobs_application','accounts_user']:
    try:
        cur.execute(f'SELECT count(*) FROM {t}')
        print(t, cur.fetchone()[0])
    except Exception as e:
        print('err',t,e)
for t in ['jobs_job','jobs_application']:
    try:
        cur.execute(f'PRAGMA table_info({t})')
        print('cols',t,cur.fetchall())
    except Exception as e:
        print('err schema',t,e)
for t in ['jobs_job','jobs_application']:
    try:
        cur.execute(f'SELECT * FROM {t} LIMIT 5')
        print('rows',t,cur.fetchall())
    except Exception as e:
        print('err rows',t,e)
con.close()
