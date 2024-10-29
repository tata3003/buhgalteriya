from application.salary import *
from application.db.people import *
from datetime import datetime

if __name__ == '__main__':
    print("Текущая дата:", datetime.now().strftime("%Y-%m-%d"))
    calculate_salary()
    get_employees()
