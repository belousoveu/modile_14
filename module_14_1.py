from UserRepository import UserRepository

repo = UserRepository()

for i in range(10):
    repo.add_user("user" + str(i + 1), "example" + str(i + 1) + "@gmail.com", (i + 1) * 10, 1000)

users = repo.get_all_users()

for i in range(0, 10, 2):
    repo.update_balance(users[i][0], 500)

users = repo.get_all_users()

for i in range(0, 10, 3):
    repo.delete_user(users[i][0])

users = repo.find_users_by_age_not_equal_to(60)
for user in users:
    print(user)

repo.close()
