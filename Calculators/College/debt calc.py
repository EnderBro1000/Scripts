debt = 95000
interest_percent = .059
yearly_salary = None
hourly_salary = 20
debt_repayment_percent = .2
debt_repayment_length = 0
work_days = 261
work_hours = 8
interest = 0

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
