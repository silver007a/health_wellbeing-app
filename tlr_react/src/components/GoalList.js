import React from "react"
import './style/GoalList.css'

const GoalList = ({allGoals, onGoalClick}) => {

    const allGoalsListed = allGoals.map((agoal) => {
      return <li><button id="goal-button" onClick={() => onGoalClick(agoal)}>{agoal.name}</button></li>
    })

      return (
        <nav>
          <section id ="logo-text">
            <h2>TLR Dashboard</h2>
          </section>
          <ul>
            {allGoalsListed}
          </ul>
        </nav>
)}

export default GoalList