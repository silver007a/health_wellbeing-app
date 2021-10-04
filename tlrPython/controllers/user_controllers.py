from flask import Flask, request, redirect, jsonify
from werkzeug.utils import redirect
from repositories import user_repository
from models.user import User
from helpers.serializers import *
from flask import Blueprint

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route('/users')
def all_users():
    users = user_repository.select_all()
    users_json = []
    for user in users:
        serialized_user = serialize_user(user)
        users_json.append(serialized_user)
    return jsonify(users_json)


# NEW
# GET '/goals/new'
# @milestone_blueprint.route("/goals/new")
# def new_milestone():
#     goal = goal_repository.select_all()   
#     return render_template("goals/new.html", all_goals=goal)


# # CREATE
# # POST '/goals'
# @milestone_blueprint.route("/goals", methods=["POST"])
# def create_milestone():
#     mile_title = request.form["mile_title"]
#     mile_desc = request.form["mile_desc"]
#     mile_position = request.form["mile_position"]
#     mile_date = request.form["mile_date"]
#     goal_id = request.form["goal_id"]
#     goal = goal_repository.select(goal_id)
#     new_milestone = Milestone(mile_title, mile_desc, mile_position, mile_date, goal)
#     milestone_repository.save(new_milestone)  
#     return redirect("/")


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