import React from "react";
import './style/MilestonesList.css'

const MilestoneList = ({allMilestones}) => {
    
    const allMilestonesListed = allMilestones.map((amilestone) => {
        
        return <p id="milestone-list"><b>Milestone: </b> {amilestone.mileDesc}<br/><br/> <b>Deadline: </b>{amilestone.mileDate}</p>
    })
    return (
        <>
            <div>{allMilestonesListed}</div>
        </>
)}

export default MilestoneList