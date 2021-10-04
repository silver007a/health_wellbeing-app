from flask import Flask, request, redirect, jsonify
from werkzeug.utils import redirect
from repositories import goal_repository
from helpers.serializers import *
from flask import Blueprint
from models.goal import Goal
from models.user import User

goal_blueprint = Blueprint("goal", __name__)

@goal_blueprint.route('/goals')
def all_goals():
    goals = goal_repository.select_all()
    goals_json = []
    for goal in goals:
        serialized_goal = serialize_goal(goal)
        goals_json.append(serialized_goal)    
    return jsonify(goals_json)


# POST '/goals'
@goal_blueprint.route("/api/goals", methods=["POST"])
def create_goal():
    data = request.json
    name = data["name"]
    description = data["description"]
    goal_date = data["goal_date"]
    user = User("James", "at@gg.com", data["user_id"])
    new_goal = Goal(name, description, goal_date, user)
    print(f"this is thwe goal: {new_goal}")
    goal_repository.save(new_goal)  
    return redirect("/")

# @app.route('/goals/new')# def create_goal():
#     goals = goal_repository.select_all()
#     goals_json = []
#     for goal in goals:
#         serialized_goal = serialize_goal(goal)
#         goals_json.append(serialized_goal)
#     return jsonify(goals_json)

# NEW
# GET '/goals/new'
# @milestone_blueprint.route("/goals/new")
# def new_milestone():
#     goal = goal_repository.select_all()
#     return render_template("goals/new.html", all_goals=goal)


# # CREATE


# # SHOW
# # GET '/goals/<id>'
# @milestone_blueprint.route("/goals/<id>", methods=['GET'])
# def show_milestone(id):
#     milestone = milestone_repository.select(id)
#     return render_template('goals/show.html', milestone = milestone)


# # EDIT
# # GET '/goals/<id>/edit'
# @milestone_blueprint.route("/goals/<id>/edit", methods=['GET'])
# def edit_milestone(id):
#     milestone = milestone_repository.select(id)
#     goals = goal_repository.select_all()
#     return render_template('goals/edit.html', milestone = milestone, all_goals = goals)


# # UPDATE
# # PUT '/goals/<id>'
# @milestone_blueprint.route("/goals/<id>", methods=['POST'])
# def update_milestone(id):
#     mile_title = request.form["mile_title"]
#     mile_desc = request.form["mile_desc"]
#     mile_position = request.form["mile_position"]
#     mile_date = request.form["mile_date"]
#     goal_id = request.form["goal_id"]
#     goal = goal_repository.select(goal_id)
#     milestone = Milestone(mile_title, mile_desc, mile_position, mile_date, goal, id)
#     milestone_repository.update(milestone)
#     return redirect('/')

    
# # DELETE
# # DELETE '/goals/<id>'
# @milestone_blueprint.route("/goals/<id>/delete", methods=["POST"])
# def delete_milestone(id):
#     milestone_repository.delete(id)
#     return redirect("/")