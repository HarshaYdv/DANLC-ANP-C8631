# Wap to calculate the salary slip
# Basic  salary : input from user  // salary=60000
# Da     :    2% of basic   // da=0.02*salary
# Ta     :    3% of salary
# Hra    :    10% salary
# PF     :    15% of salary
# Total salary  =   basic+da+ta+hra+pf;
# Net salary    =   total-pf;
# Calculate bonus of employee to 25 % of salary by shift operators.

basic_salary = int(input("Enter your basic salary : "))
print("Basic Salary : ", basic_salary)

da = 0.02 * basic_salary
print("DA : ", da)

ta = 0.03 * basic_salary
print("TA : ", ta)

hra = 0.1 * basic_salary
print("HRA : ", hra)

pf = 0.15 * basic_salary
print("PF : ", pf)

total_salary = basic_salary + da + ta + hra + pf
print("Total Salary : ", total_salary)

net_salary = total_salary - pf
print("Net Salary : ", net_salary)

# bonus = basic_salary * 0.25
bonus = basic_salary >> 2
print("Bonus : ", bonus)
