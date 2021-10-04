import React, {useState} from "react"
import MilestoneList from "./MilestoneList"
import SmashList from "./SmashList"
import Button from "react-bootstrap/Button"  
import Modal from "react-bootstrap/Modal"
import { postGoal } from "./GoalService"
import './style/GoalDetails.css'


const GoalDetail = ({selectedGoal, setCountMilestones, setCountSmashs, totalScores, addGoal}) => {
    const milestoneScore = selectedGoal.milestones.length * 2
      setCountMilestones(milestoneScore)
    const smashScore = selectedGoal.smashs.length * 3
      setCountSmashs(smashScore)

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const [formData, setFormData] = useState({})
  
    const onChange = (e) =>{
      formData[e.target.id] = e.target.value;
      setFormData(formData);
    }

    const onSubmit = (e) =>{
      e.preventDefault();
      postGoal(formData).then((data)=>{
      addGoal(data);
    })
    }


    return(
      <section id="data-view">
        <section id="goals-back">
          <section id="goals-view">

            <section id ="update">
              <Button id="update-button" onClick={handleShow}>Add Goal</Button>
              <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                  <Modal.Title>Add New Goal</Modal.Title>
                </Modal.Header>
                  
              <form onSubmit={onSubmit} id="goal-form" >
                <Modal.Body>
                  <div className="formWrap">
                    <label htmlFor="name">Name:</label>
                    <input onChange={onChange} type="text" id="name"  />
                  </div>
                  <div className="formWrap">
                    <label htmlFor="description">Description:</label>
                    <input onChange={onChange} type="text" id="description"  />
                  </div>
                  <div className="formWrap">
                    <label htmlFor="date">Date:</label>
                    <input onChange={onChange} type="date" id="goal_date"  />
                  </div>
                </Modal.Body>
                
                <Modal.Footer>
                  <input class="update-button" type="submit" value="Save" id="save" onClick={handleClose}/>
                  <input class="update-button" type="submit" value="Close" onClick={handleClose}/> 
                </Modal.Footer>
              </form>
                </Modal>
            </section>

              <h2>Goal:</h2>

              <div id="scores">
                <p>Score Total: {totalScores}/100 points</p>
              </div>
                <h3>{selectedGoal.name}</h3>
                <p>{selectedGoal.description}</p>
                <p><b>Deadline:</b> {selectedGoal.goalDate}</p>
          
          </section>
        </section>

          <section id="goals-back">
            <section id="milestones-view">
              <h2>Milestones:</h2>
              <div id="scores">
                <p>Score: {milestoneScore} points </p>
              </div>
                <MilestoneList  allMilestones={selectedGoal.milestones}/>
            </section>
          </section>

          <section id="goals-back">
            <section id="smashs-view">
              <h2>If-Then:</h2>
              <div id="scores">
                <p>Score: {smashScore} points </p>
              </div>

                <SmashList  allSmashs={selectedGoal.smashs}/>
            </section>
          </section>
         

      </section> 
)}

export default GoalDetail