from flask import Flask, request, redirect, jsonify
from werkzeug.utils import redirect
from repositories import goal_repository, milestone_repository, minihabit_repository
from models.user import User
from helpers.serializers import *
from flask import Blueprint

minihabit_blueprint = Blueprint("minihabit", __name__)

@minihabit_blueprint.route('/minihabits')
def all_minihabits():
    minihabits = minihabit_repository.select_all()
    minihabits_json = []
    for minihabit in minihabits:
        serialized_minihabit = serialize_minihabit(minihabit)
        minihabits_json.append(serialized_minihabit)
    return jsonify(minihabits_json)


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