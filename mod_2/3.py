# Задача 3. Контроль
employee_ids = []
num_employee = int(input("Введите количество сотрудников: "))
for i in range(num_employee):
    worker_id = int(input("ID сотрудника: "))
    employee_ids.append(worker_id)
    num_employee += 1
print(employee_ids)
target_employee_id = int(input("Введите ID нужного сотрудника: "))
if target_employee_id in employee_ids:
    print(f"Сотрудник на месте")
else:
    print("Сотрудник НЕ на месте")

