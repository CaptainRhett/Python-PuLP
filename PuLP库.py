import pulp
first_lpproblem = pulp.LpProblem("mf_first_lp",sense = pulp.LpMaximize)
x1 = pulp.LpVariable('x1',lowBound=0,upBound=7,cat="continuous")
x2 = pulp.LpVariable('x2',lowBound=0,upBound=7,cat="continuous")
x3 = pulp.LpVariable('x3',lowBound=0,upBound=7,cat="continuous")
first_lpproblem +=2*x1 + 3*x2 -5*x3
first_lpproblem +=(2*x1 -5*x2 + x3 >=10)
first_lpproblem +=(x1 +x2+x3 == 7)
first_lpproblem +=(x1 +3*x2 +x3 <= 12)
first_lpproblem.solve()
print("Status :",pulp.LpStatus[first_lpproblem.status])
for i in first_lpproblem.variables():
    print(i.name , "=" , i.varValue)
print("F(x) = " , pulp.value(first_lpproblem.objective))