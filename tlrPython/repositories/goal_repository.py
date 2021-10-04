from db.run_sql import run_sql
from models.user import User
from models.goal import Goal
from models.milestone import Milestone
import repositories.user_repository as user_repository


def save(goal):
    sql = "INSERT INTO goals (name, description, goal_date, users_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [goal.name, goal.description, goal.goal_date, goal.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    goal.id = id
    return goal


def select_all():
    goals = []
    sql = "SELECT * FROM goals"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row['users_id'])
        goal = Goal(row['name'], row['description'], row['goal_date'], user, row['id'] )
        goals.append(goal)
    return goals


def select(id):
    goal = None
    sql = "SELECT * FROM goals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        user = user_repository.select(result['users_id'])
        goal = Goal(result['name'], result['description'], result['goal_date'], user, result['id'] )
    return goal


def delete_all():
    sql = "DELETE FROM goals"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM goals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(goal):
    sql = "UPDATE goals SET (name, description, goal_date) = (%s, %s, %s) WHERE id = %s"
    values = [goal.name, goal.description, goal.goal_date, goal.id]
    run_sql(sql, values)


def milestones(goal):
    milestones = []
    sql = "SELECT * FROM milestone WHERE goal_id = %s"
    values = [goal.id]
    results = run_sql(sql, values)
    for row in results:
        milestone = Milestone(row['mile_desc'], row['mile_date'], row['goal_id'] )
        milestones.append(milestone)
    return milestones