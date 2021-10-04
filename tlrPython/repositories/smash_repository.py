from db.run_sql import run_sql
from models.goal import Goal
from models.smash import Smash
import repositories.goal_repository as goal_repository


# def save(goal):
#     sql = "INSERT INTO goals (name, description, goal_date, users_id) VALUES (%s, %s, %s, %s) RETURNING *"
#     values = [goal.name, goal.description, goal.goal_date, goal.user.id]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     goal.id = id
#     return goal


def select_all():
    smashs = []
    sql = "SELECT * FROM smashs"
    results = run_sql(sql)
    for row in results:
        goal = goal_repository.select(row['goal_id'])
        smash = Smash(row['problem'], row['solution'], goal, row['id'] )
        smashs.append(smash)
    return smashs


# def select(id):
#     goal = None
#     sql = "SELECT * FROM goals WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]
#     if result is not None:
#         user = user_repository.select(result['users_id'])
#         goal = Goal(result['name'], result['description'], result['goal_date'], user, result['id'] )
#     return goal


# def delete_all():
#     sql = "DELETE FROM goals"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM goals WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(goal):
#     sql = "UPDATE goals SET (name, description, goal_date) = (%s, %s, %s) WHERE id = %s"
#     values = [goal.name, goal.description, goal.goal_date, goal.id]
#     run_sql(sql, values)


def find_by_goal_id(goal_id):
    smashs = []
    sql = "SELECT * FROM smashs WHERE goal_id = %s ORDER BY id"
    values = [goal_id]
    results = run_sql(sql, values)
    for row in results:
        smash = Smash(row['problem'], row['solution'], None, row['id'])
        smashs.append(smash)
    return smashs