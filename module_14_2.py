from UserRepository import UserRepository

repo = UserRepository()

repo.delete_user(6)

count = repo.count()
total = repo.get_total_balance()

print(f"Всего записей: {count}.")
print(f"Суммарный баланс: {total}")
print(f"Среднее значение баланса: {total/count}")

users = repo.get_all_users()

repo.close()
