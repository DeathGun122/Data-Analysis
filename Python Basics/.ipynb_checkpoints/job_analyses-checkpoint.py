def calculate_salary(base_salary, bonus_rate = 0.1):
    return base_salary * (1 + bonus_rate)

def bonus(total_salary, base_salary):
    return (total_salary - base_salary) / base_salary

def cal_bonus(total_salary, base_salary):
    return (total_salary - base_salary) / base_salary