import React from "react";
import './style/SmashList.css'

const SmashList = ({allSmashs}) => {
    
    const allSmashsListed = allSmashs.map((asmash) => {
        return <p id="smash-list"><b>Problem: </b>{asmash.problem} <br/><br/><b>Solution: </b>{asmash.solution}</p>
    })
    return (
        <>
            {allSmashsListed}
        </>
)}

export default SmashList