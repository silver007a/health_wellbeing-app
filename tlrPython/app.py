from flask import Flask, jsonify
from controllers.milestone_controllers import milestone_blueprint
from controllers.goal_controllers import goal_blueprint
from controllers.minihabit_controllers import minihabit_blueprint
from controllers.user_controllers import user_blueprint
from controllers.task_controllers import task_blueprint
from controllers.smash_controllers import smash_blueprint
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(milestone_blueprint)
app.register_blueprint(goal_blueprint)
app.register_blueprint(minihabit_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(task_blueprint)
app.register_blueprint(smash_blueprint)


# @app.route('/')
# def homepage():
#     milestones = milestone_repository.select_all()
#     return render_template("index.html", all_milestones = milestones)

# @app.route('/goals')
# def home():
#     milestones = milestone_repository.select_all()
#     return render_template("goals/home.html", all_milestones = milestones)

if __name__ == '__main__':
    app.run(debug=True)