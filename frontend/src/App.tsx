import axios from 'axios'
import { useEffect, useState } from 'react';
import './App.css';

interface ToDo {
  content: string
  complete: boolean
}

function App() {

  const [todos,setTodos] = useState<ToDo[]>()

  useEffect(()=>{
    const fetchData = async () =>{
      const data = await axios.get('http://127.0.0.1:5000/')
      setTodos(data.data)
    }
    fetchData()
  },[])

  return (
    <>
      {todos?.map(todo=><p>{todo.content}</p>)}
    </>
  );
}

export default App;
