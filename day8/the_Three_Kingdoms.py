import mysql.connector

def p(value):
    for i in value:
        print(i)

# 创建数据库连接
conn = mysql.connector.connect(user='root', password='hzj522zy.', database='company')

# 初始化数据库连接对象
cursor = conn.cursor()

# 查询出部门编号为30的所有员工
cursor.execute('select * from t_employees where deptno = 30 ')
values = cursor.fetchall()
print('查询出部门编号为30的所有员工')
print(p(values))

# 所有经理的姓名、编号和部门编号
cursor.execute('select empno,ename,deptno from t_employees where job="经理"')
values = cursor.fetchall()
print('查询所有经理的姓名、编号和部门编号')
print(p(values))

# 找出奖金高于工资的员工
cursor.execute('select ename,sal,comm from t_employees where comm > sal')
values = cursor.fetchall()
print('找出奖金高于工资的员工')
print(p(values))

# 找出奖金高于工百分之60的员工
cursor.execute('select ename,sal,comm from t_employees where comm > (sal*0.6)')
values = cursor.fetchall()
print('找出奖金高于工资的员工')
print(p(values))

# 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料
cursor.execute('select * from t_employees where deptno=10 and job="经理" or deptno=20 and job="分析员"')
print('找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料')
values = cursor.fetchall()
print(p(values))

# 找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料。
cursor.execute('select * from t_employees where (deptno=10 and job="经理") or (deptno=20 and job="分析员") or (job not IN ('
               '"经理","武装上将")) and sal>=3000')
values = cursor.fetchall()
print('找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料')
print(p(values))

# 找出无奖金或奖金低于1000的员工
cursor.execute('select ename from t_employees where comm is null or comm<1000')
values = cursor.fetchall()
print('找出无奖金或奖金低于1000的员工')
print(p(values))

# 查询名字由三个字组成的员工
cursor.execute('select ename from t_employees where length(ename)=9')
values = cursor.fetchall()
print('查询名字由三个字组成的员工')
print(p(values))

# 查询2000年以后入职的员工
cursor.execute('select ename,hiredate from t_employees where hiredate>=20000101')
values = cursor.fetchall()
print('查询2000年以后入职的员工')
print(p(values))

# 查询所有员工详细信息，用编号升序排序
cursor.execute('select * from t_employees order by empno')
values = cursor.fetchall()
print('查询所有员工详细信息，用编号升序排序')
print(p(values))

# 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
cursor.execute('select * from t_employees order by comm desc , hiredate asc')
values = cursor.fetchall()
print('查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序')
print(p(values))

# 查询每个部门的平均工资
cursor.execute('select deptno,avg(sal) from t_employees group by deptno')
values = cursor.fetchall()
print('查询每个部门的平均工资')
print(p(values))

# 查询每个部门的雇员数量
cursor.execute('select deptno,count(deptno) from t_employees group by deptno')
values = cursor.fetchall()
print('查询每个部门的雇员数量')
print(p(values))

# 查询每种工作的最高工资、最低工资、人数
cursor.execute('select job,max(sal),min(sal) from t_employees group by job')
values = cursor.fetchall()
print('查询每种工作的最高工资、最低工资、人数')
print(p(values))

# 关闭连接
cursor.close()