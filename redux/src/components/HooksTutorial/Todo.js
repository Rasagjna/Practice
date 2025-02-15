import React from 'react'
import { ACTIONS } from './UseReducerHook'

function Todo({todo,dispatch}) {
  return (
    <div>
        <span style={{color:todo.complete?"#AAA": '#00'}}>{todo.name}</span>
        <button onClick={() => dispatch({type:ACTIONS.TOGGLE_TODO, payload:{id:todo.id}})}>Toggle</button>
        <button> Delete</button>
    </div>
  )
}

export default Todo