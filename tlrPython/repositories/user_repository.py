from db.run_sql import run_sql
from models.user import User
from models.goal import Goal


def save(user):
    sql = "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING *"
    values = [user.name, user.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user


def select_all():
    users = []
    sql = "SELECT * FROM users"
    results = run_sql(sql)
    for row in results:
        user = User(row['name'], row['email'], row['id'] )
        users.append(user)
    return users


def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = User(result['name'], result['email'], result['id'] )
    return user


def delete_all():
    sql = "DELETE  FROM users"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(user):
    sql = "UPDATE goals SET (name, email) = (%s, %s) WHERE id = %s"
    values = [user.name, user.email, user.id]
    run_sql(sql, values)


def goals(user):
    goals = []
    sql = "SELECT * FROM goal WHERE users_id = %s"
    values = [user.id]
    results = run_sql(sql, values)
    for row in results:
        goal = Goal(row['name'], row['description'], row['goal_date'], row['users_id'] )
        goals.append(goal)
    return goals