from webhandler import get, post
from model.database import Database
from model.employee import Employee

@get('/')
def index():
    return {
        '__template__': 'employee_list.html'

    }

@get('/services/employees')
def get_employees():
    emps = Database.query_employee()
    return dict(employees = emps)

@get('/ui/employees/add')
def ui_add_employee():
    return {
        '__template__': 'add_edit_employee.html',
        'id': '',
        'action': '/services/employees'
    }

@post('/services/employees')
def add_employee(*, code, name):
    employee = Employee(code, name)
    Database.save_employee(employee)

@get('/ui/employees/edit')
def ui_edit_employee(*, id):
    return {
        '__template__': 'add_edit_employee.html',
        'id': id,
        'action': '/services/employees/%s' % id
    }

@get('/services/employees/{id}')
def query_employee(*, id):
    employee = Database.query_by_id(id)
    print(employee)
    return dict(id=employee[0], code=employee[1], name=employee[2])

@post('/services/employees/{id}')
def update_employee(*, id, code, name):
    emp = Employee(code, name)
    emp.id = id
    Database.update(emp)

@post('/services/employees/{id}/delete')
def delete_employee(*, id):
    Database.delete(id)