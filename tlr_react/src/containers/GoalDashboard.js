import React, { useState, useEffect} from "react"
import GoalDetail from "../components/GoalDetail"
import GoalList from "../components/GoalList"
import './GoalDashboard.css'

const GoalDashboard = () => {

    const [selectedGoal, setSelectedGoal] = useState(null)
    const [countMilestones, setCountMilestones] = useState(0) 
    const [countSmashs, setCountSmashs] = useState(0)
    const [goalsApi, setGoalsApi] = useState([])
    const [totalScores, setTotalScores] = useState(0)
                               
    useEffect(() => {
    fetchGoal();
    }, [])


    const fetchGoal =  function() {
    fetch("http://127.0.0.1:5000/goals")
    .then(async(response) => {
    const data = await response.json() 
        return data})
    .then(data => {setGoalsApi(data)})
    }


    useEffect(() => {
      const newTotal = countMilestones + countSmashs//+ component
    setTotalScores(newTotal) 
    }, [countMilestones, countSmashs])
    

    const onGoalSelected = function(goala) {
    setSelectedGoal(goala);
    }
   

    if (!goalsApi || goalsApi.length === 0) {
      return <p>...loading</p>
    }


    return ( 
      <div id="screen">
        <GoalList  allGoals={goalsApi} onGoalClick={onGoalSelected} />
        {selectedGoal ? <GoalDetail totalScores={totalScores} setCountSmashs={setCountSmashs} setCountMilestones={setCountMilestones} selectedGoal={selectedGoal} /> : null}
      </div>
)}

export default GoalDashboard