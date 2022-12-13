import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []

    try:
        conn=psycopg2.connect("dbname='music_library'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results

def show_table(table_name):
    sql = "SELECT * FROM " + table_name
    results = run_sql(sql)
    return results

def delete_all(table_name):
    sql = "DELETE FROM " + table_name
    run_sql(sql)
    
def find_by_id(the_id,the_table):
    sql = "SELECT * FROM " + the_table + " WHERE id=(%s)"
    values = [the_id]
    results = run_sql(sql, values)
    return results

