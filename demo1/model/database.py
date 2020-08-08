import mysql.connector
import configparser
from model.employee import Employee


class Database(object):
    @classmethod
    def create_connection(cls):
        config = configparser.ConfigParser()
        config.read('model/config.ini')
        USER = config.get('DB_SECTION', 'user')
        PASSWORD = config.get('DB_SECTION', 'password')
        DATABASE = config.get('DB_SECTION', 'database')
        connection = mysql.connector.connect(user=USER, password=PASSWORD, database=DATABASE, charset='utf8')
        return connection

    @classmethod
    def query_employee(cls):
        sql = 'select * from employee'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchall()
        cursor.close()
        conn.close()
        return result_set

    @classmethod
    def query_by_id(cls, id):
        sql = 'select * from employee where id = %s'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [id])
        result_set = cursor.fetchall()
        cursor.close()
        conn.close()
        if len(result_set) == 0:
            return None
        else:
            return result_set[0]

    @classmethod
    def save_employee(self, emp):
        sql = 'insert into employee (code, name) values (%s, %s)'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (emp.code, emp.name))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def update(cls, emp):
        # create sql
        sql = 'update employee set code = %s, name = %s where id = %s'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, (emp.code, emp.name, emp.id))
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def delete(cls, id):
        sql = 'delete from employee where id = %s'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, [id])
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def turacate(cls):
        sql = 'TURACATE employee'
        conn = Database.create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

if __name__ == '__main__':
    '''Database.turacate()

    # Query
    print(Database.query_employee())

    # Save
    employee = Employee('E01', 'Jacky')
    Database.save_employee(employee)

    # print(Database.query_employee())

    # Update
    employee = Employee('EC01Update', 'JackyUpdate')
    employee.id = 1
    Database.update(employee)

    print(Database.query_employee())

    # Delete
    Database.delete(1)

    print("After Delete:")
    print(Database.query_employee())'''
    id = 1
    print(Database.query_by_id(id))