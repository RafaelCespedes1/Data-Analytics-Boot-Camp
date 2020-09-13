SELECT employees.emp_no, employees.last_name, employees.first_name, 
	employees.sex, salaries.salary FROM salaries
INNER JOIN employees ON
employees.emp_no = salaries.emp_no
ORDER BY emp_no;

SELECT first_name, last_name, hire_date FROM employees
WHERE hire_date BETWEEN '1986-01-01' AND '1986-12-31'
ORDER BY emp_no;

SELECT departments.dept_no, departments.dept_name, dept_manager.emp_no,
	employees.last_name, employees.first_name 
FROM departments
	JOIN dept_manager ON (dept_manager.dept_no = departments.dept_no) 
		JOIN employees ON (dept_manager.emp_no = employees.emp_no);

SELECT employees.emp_no, employees.last_name, employees.first_name,
	departments.dept_name
FROM employees
	JOIN dept_emp ON (dept_emp.emp_no = employees.emp_no)
		JOIN departments ON (dept_emp.dept_no = departments.dept_no)
ORDER BY emp_no;

SELECT first_name, last_name, sex FROM employees
WHERE (first_name = 'Hercules') AND (last_name LIKE 'B%');

SELECT employees.emp_no, employees.last_name, employees.first_name, 
	departments.dept_name 
FROM employees
	JOIN dept_emp ON (dept_emp.emp_no = employees.emp_no)
		JOIN departments ON (dept_emp.dept_no = departments.dept_no)
WHERE dept_name = 'Sales';

SELECT employees.emp_no, employees.last_name, employees.first_name, 
	departments.dept_name 
FROM employees
	JOIN dept_emp ON (dept_emp.emp_no = employees.emp_no)
		JOIN departments ON (dept_emp.dept_no = departments.dept_no)
WHERE dept_name = 'Sales' OR dept_name = 'Development';

SELECT last_name, COUNT(last_name) FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;