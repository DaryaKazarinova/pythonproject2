'''writing user'''
def write_user(login, password, email):
    '''writing user'''
    with open("./data/users.csv", "r", encoding="utf-8") as f:
        existing_users = [l.strip("\n") for l in f.readlines()]
        title = existing_users[0]
        old_users = existing_users[1:]
    new_user_line = f"{len(old_users)+1};{login};{password};{email}"
    terms_sorted = old_users + [new_user_line]
    new_users = [title] + terms_sorted
    with open("./data/users.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_users))
