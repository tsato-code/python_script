import pulp
import random 

num_item = 10
b = 20
c = [random.randint(1, 10) for _ in range(num_item)]
a = [random.randint(1, 10) for _ in range(num_item)]

prob = pulp.LpProblem('Knapsack', pulp.LpMaximize)
x = [pulp.LpVariable(name='x{}'.format(i), cat=pulp.LpInteger, lowBound=0, upBound=1) for i in range(num_item)] # 変数の定義
obj = pulp.lpSum(c[i]*x[i] for i in range(num_item))
prob.setObjective(obj)
prob += pulp.lpSum([a[i]*x[i] for i in range(num_item)]) <= b

# 問題の書き込み
# prob.writeLP("Knapsack.lp")
prob.solve()
print("Status:", pulp.LpStatus[prob.status])
print("ObjValue = {}".format(pulp.value(prob.objective)))
for v in prob.variables():
    print(v.name, "=", v.varValue)


"""
$ python test_pulp.py
Status: Optimal
ObjValue = 35.0
x0 = 1.0
x1 = 0.0
x2 = 1.0
x3 = 1.0
x4 = 0.0
x5 = 0.0
x6 = 1.0
x7 = 0.0
x8 = 0.0
x9 = 1.0
"""