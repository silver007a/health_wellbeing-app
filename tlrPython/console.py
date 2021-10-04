import pdb
from models.milestone import Milestone
from models.goal import Goal
from models.user import User
from models.minihabit import Minihabit

import repositories.user_repository as user_repositorty
import repositories.milestone_repository as milestone_repository
import repositories.goal_repository as goal_repository
import repositories.minihabit_repository as minihabit_repository

minihabit_repository.delete_all()
milestone_repository.delete_all()
goal_repository.delete_all()
user_repositorty.delete_all()



user1 = User("James", "james@test.com")
user_repositorty.save(user1)

user2 = User("May", "someone@somewhere.com")
user_repositorty.save(user2)

goal1 = Goal("goal test1 name", "goal test desc", "2021-11-9", user1 )
goal_repository.save(goal1)
goal2 = Goal("France", "Visit Disneyland", "2021-9-12", user1)
goal_repository.save(goal2)
# goal3 = Goal("Romania", "Visit thermal spas", 1, "2021-9-12")
# goal_repository.save(goal3)

# goal_repository.select_all()

milestone_1 = Milestone("milestone description", "2021-7-12", goal1)
milestone_repository.save(milestone_1)



minihabit_1 = Minihabit("mini description", 9, user1)
minihabit_repository.save(minihabit_1)

# milestone_2 = Milestone("Write a short plan for saving", "Create a shared document in Google drive and list todo.", 1, "July", goal1)
# milestone_repository.save(milestone_2)

# milestone_3 = Milestone("Get the car seviced ready to go", "Phone the garage and get the car booked in and get tyres checked.", 1, "July", goal1)
# milestone_repository.save(milestone_3)

# milestone_4 = Milestone("Set up a savings account", "Research best savings accounts online.", 2, "Wed 4th", goal1)
# milestone_repository.save(milestone_4)

# milestone_5 = Milestone("Research places to go and see", "Go to library and get some travel books on Disneyland and region.", 12, "2pm tomorrow", goal2)
# milestone_repository.save(milestone_5)

# milestone_6 = Milestone("Learn to speak some French", "Look for online course and intercambios on meetup groups.", 4, "By next week 4th", goal2)
# milestone_repository.save(milestone_6)

# milestone_7 = Milestone("Find out if there are other places to visit", "Contact some friends who live there (Julie and Martin) and ask where are the best places to visit.", 2, "2021-10-12", goal1)
# milestone_repository.save(milestone_7)

# milestone_8 = Milestone("Buy a new camera for trip", "Go online and look for some reviews on action pros and action cameras that can get wet.", 7, "2021-9-12", goal1)
# milestone_repository.save(milestone_8)

# milestone_9 = Milestone("Look for reviews online", "Go to Trip Advisor and websites like that and find out what is good to do and see.", 6, "July 5th", goal3)
# milestone_repository.save(milestone_9)

# milestone_10 = Milestone("Contact Julie to arrange to meet up there", "Give Julie a call on Monday and arrange to visit.", 9, "Wednesday 15th", goal3)
# milestone_repository.save(milestone_10)

# milestone_11 = Milestone("Find out about insurance policy", "Check the bank insurance policy and that we are covered for France.", 2, "By weekend", goal2)
# milestone_repository.save(milestone_11)

# milestone_12 = Milestone("Book some hotels and restaurants", "Get a Michelin review online or at the library and find and book some of the best places.", 2, "By weekend", goal3)
# milestone_repository.save(milestone_12)

# milestone_13 = Milestone("Go to the islands and castles", "Look for haunted castles and shows to make it fun for the kids and family", 2, "By weekend", goal1)
# milestone_repository.save(milestone_13)

# milestone_14 = Milestone("Buy a new camera for trip", "Go online and look for some reviews on action pros and action cameras that can get wet.", 7, "2021-9-12", goal2)
# milestone_repository.save(milestone_14)

# milestone_15 = Milestone("Look for reviews online", "Go to Trip Advisor and websites like that and find out what is good to do and see.", 6, "July 5th", goal3)
# milestone_repository.save(milestone_15)

# milestone_16 = Milestone("Contact Julie to arrange to meet up there", "Give Julie a call on Monday and arrange to visit.", 9, "Wednesday 15th", goal3)
# milestone_repository.save(milestone_16)

# milestone_17 = Milestone("Find out about insurance policy", "Check the bank insurance policy and that we are covered for France.", 2, "By weekend", goal2)
# milestone_repository.save(milestone_17)

# milestone_18 = Milestone("Book some hotels and restaurants", "Get a Michelin review online or at the library and find and book some of the best places.", 2, "By weekend", goal3)
# milestone_repository.save(milestone_18)

# milestone_19 = Milestone("Go to the islands and castles", "Look for haunted castles and shows to make it fun for the kids and family", 2, "By weekend", goal2)
# milestone_repository.save(milestone_19)

# milestone_20= Milestone("Buy a new camera for trip", "Go online and look for some reviews on action pros and action cameras that can get wet.", 7, "2021-9-12", goal1)
# milestone_repository.save(milestone_20)

# milestone_21 = Milestone("Look for reviews online", "Go to Trip Advisor and websites like that and find out what is good to do and see.", 6, "July 5th", goal2)
# milestone_repository.save(milestone_21)

# milestone_22 = Milestone("Contact Julie to arrange to meet up there", "Give Julie a call on Monday and arrange to visit.", 9, "Wednesday 15th", goal3)
# milestone_repository.save(milestone_22)

# milestone_23 = Milestone("Find out about insurance policy", "Check the bank insurance policy and that we are covered for France.", 2, "By weekend", goal2)
# milestone_repository.save(milestone_23)

# milestone_24 = Milestone("Book some hotels and restaurants", "Get a Michelin review online or at the library and find and book some of the best places.", 2, "By weekend", goal3)
# milestone_repository.save(milestone_24)

# milestone_25 = Milestone("Go to the islands and castles", "Look for haunted castles and shows to make it fun for the kids and family", 2, "By weekend", goal2)
# milestone_repository.save(milestone_25)


# pdb.set_trace()
