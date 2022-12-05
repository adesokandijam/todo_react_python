import React , {useEffect, useState} from 'react'

function App (){
  const [todo, setTodo] = useState("")

  useEffect(() => {
    fetch("/api/todo/123").then(res => res.json()).then(data => {
      setTodo(data.todo)
      console.log(data.todo)
    });
  },[])
  return (
    <div>
      <h1>What I have to do</h1>
      <h2>{todo}</h2>
    </div>
  )
}

export default App