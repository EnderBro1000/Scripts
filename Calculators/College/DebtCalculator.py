debt = int(input('Debt: '))
interest_percent = int(input('Percentage of Interest: '))
yearly_salary = int(input('Yearly Salary: '))
hourly_salary = int(input('Hourly Salary: '))
debt_repayment_percent = int(input('Debt Repayment Percent: '))
debt_repayment_length = int(input('Debt Repayment Length: '))
work_days = int(input('Work Days: '))
work_hours = int(input('Work Hours: '))
interest = int(input('Interest: '))

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
