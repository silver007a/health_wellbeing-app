from repositories import milestone_repository
from repositories import smash_repository
from datetime import datetime

def serialize_user(user):
    userDict = {}
    userDict["name"] = user.name
    userDict["email"] = user.email
    return userDict

def serialize_goal(goal):
    goalDict = {}
    goalDict["name"] = goal.name
    goalDict["description"] = goal.description
    goalDict["goalDate"] = goal.goal_date
    
    milestones_for_goal = milestone_repository.find_by_goal_id(goal.id)
    milestones_json = []
    for milestone in milestones_for_goal:
        serialized_milestone = serialize_milestone(milestone)
        milestones_json.append(serialized_milestone)
    goalDict["milestones"] = milestones_json
    
    smashs_for_goal = smash_repository.find_by_goal_id(goal.id)
    smashs_json = []
    for smash in smashs_for_goal:
        serialized_smash = serialize_smash(smash)
        smashs_json.append(serialized_smash)
    goalDict["smashs"] = smashs_json
    return goalDict


def serialize_milestone(milestone):
    milestoneDict = {}
    milestoneDict["mileDesc"] = milestone.mile_desc
    milestoneDict["mileDate"] = milestone.mile_date
    return milestoneDict


def serialize_smash(smash):
    smashDict = {}
    smashDict["problem"] = smash.problem
    smashDict["solution"] = smash.solution
    return smashDict


def serialize_task(task):
    taskDict = {}
    taskDict["taskName"] = task.task_name
    taskDict["taskDesc"] = task.task_desc
    taskDict["taskDate"] = task.task_date
    taskDict["userId"] = task.user.id
    return taskDict


def serialize_minihabit(minihabit):
    minihabitsDict = {}
    minihabitsDict["miniDesc"] = minihabit.mini_desc
    minihabitsDict["miniScore"] = minihabit.mini_score
    minihabitsDict["userId"] = minihabit.user.id
    return minihabitsDict


