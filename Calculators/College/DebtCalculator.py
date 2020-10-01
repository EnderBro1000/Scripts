debt = input('Debt: ')
interest_percent = input('Percentage of Interest: ')
yearly_salary = input('Yearly Salary: ')
hourly_salary = input('Hourly Salary: ')
debt_repayment_percent = input('Debt Repayment Percent: ')
debt_repayment_length = input('Debt Repayment Length: ')
work_days = input('Work Days: ')
work_hours = input('Work Hours: ')
interest = input('Interest: ')

if yearly_salary and hourly_salary is not None:
    if yearly_salary != hourly_salary * work_days * work_hours:
        raise ValueError('only yearly or hourly salary can be defined')

if yearly_salary is None:
    yearly_salary = hourly_salary * (work_days * work_hours)
else:
    hourly_salary = yearly_salary / (work_days * work_hours)

while debt > 0:
    debt_repayment_length += 1
    debt *= 1 + interest_percent * (1 / 12)
    interest += debt * (1 + interest_percent * (1 / 12)) - debt
    debt -= yearly_salary / 12 * debt_repayment_percent

print(f'{debt_repayment_length} months, paying ${round(interest)} in interest')
