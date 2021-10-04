from db.run_sql import run_sql
from models.user import User 
from models.minihabit import Minihabit
import repositories.user_repository as user_repository


def save(minihabit):
    sql = "INSERT INTO minihabits (mini_desc, mini_score, users_id) VALUES (%s, %s, %s) RETURNING *"
    values = [minihabit.mini_desc, minihabit.mini_score, minihabit.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    minihabit.id = id
    return minihabit


def select_all():
    minihabit = []
    sql = "SELECT * FROM minihabits"
    results = run_sql(sql)
    for row in results:
        user = user_repository.select(row['users_id'])
        minihabits = Minihabit(row['mini_desc'], row['mini_score'], user, row['id'] )
        minihabit.append(minihabits)
    return minihabit


def select(id):
    minihabit = None
    sql = "SELECT * FROM minihabits WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        minihabit = Minihabit(result['mini_desc'], result['mini_score'], result['id'] )
    return minihabit


def delete_all():
    sql = "DELETE FROM minihabits"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM minihabits WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(minihabit):
    sql = "UPDATE minihabit SET (mini_desc, mini_score) = (%s, %s, %s) WHERE id = %s"
    values = [minihabit.mini_desc, minihabit.mini_score, minihabit.users.id]
    run_sql(sql, values)


def minihabits(users):
    minihabits = []
    sql = "SELECT * FROM minihabits WHERE user_id = %s"
    values = [users.id]
    results = run_sql(sql, values)
    for row in results:
        minihabit = Minihabit(row['mini_desc'], row['mini_score'], row['goal_id'] )
        minihabits.append(minihabit)
    return minihabits