const baseURL = 'http://localhost:5000/api/goals'

export const getGoals = () => {
    return fetch(baseURL)
        .then(res => res.json())
}

export const postGoal = (payload) => {
    payload.user_id = 1  
    return fetch(baseURL, {
        
        method: 'POST',
        body: JSON.stringify(payload),
        headers: { 'Content-Type': 'application/json' },
        mode: "cors" 
    })
    
    .then(res => res.json())
}

export const deleteGoal = (id) => {
    return fetch(baseURL + id, {
        method: 'DELETE'
    })
}

