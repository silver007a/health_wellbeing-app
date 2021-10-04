from db.run_sql import run_sql
from models.milestone import Milestone
from models.goal import Goal
import repositories.goal_repository as goal_repository


def save(milestone):
    sql = "INSERT INTO milestones (mile_desc, mile_date, goal_id) VALUES (%s, %s, %s) RETURNING *"
    values = [milestone.mile_desc, milestone.mile_date, milestone.goal.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    milestone.id = id
    return milestone


def select_all():
    milestones = []
    sql = "SELECT * FROM milestones ORDER BY mile_date"
    results = run_sql(sql)
    for row in results:
        goal = goal_repository.select(row['goal_id'])
        milestone = Milestone(row['mile_desc'], row['mile_date'], goal, row['id'])
        milestones.append(milestone)
    return milestones


def select(id):
    milestone = None
    sql = "SELECT * FROM milestones WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        milestone = Milestone(result['mile_desc'], result['mile_date'], result['id'])
    return milestone


def delete_all():
    sql = "DELETE  FROM milestones"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM milestones WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(milestones):
    sql = "UPDATE milestones SET (mile_desc, mile_date, goal_id) = (%s, %s) WHERE id = %s"
    values = [milestones.mile_desc, milestones.mile_date, milestones.id,]
    run_sql(sql, values)


def find_by_goal_id(goal_id):
    milestones = []
    sql = "SELECT * FROM milestones WHERE goal_id = %s ORDER BY mile_date"
    values = [goal_id]
    results = run_sql(sql, values)
    for row in results:
        milestone = Milestone(row['mile_desc'], row['mile_date'], None, row['id'])
        milestones.append(milestone)
    return milestones