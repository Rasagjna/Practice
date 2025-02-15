import React from 'react'
import { useState } from 'react'
import ClassContextComponent from './ClassContextComponent'
import FunctionContextComponent from '../FunctionContextComponent'
export const ThemeContext = React.createContext()
function UseContextHook() {
    const [darkTheme,setDarkTheme] = useState(true)
    function toggleTheme(){
        setDarkTheme(prevDarkTheme => !prevDarkTheme)
    }
  return (
    <div>
        <ThemeContext.Provider value={darkTheme}>
        <button onClick = {toggleTheme}>Toggle Theme</button>
        <FunctionContextComponent />
        <ClassContextComponent/>
        </ThemeContext.Provider>
    </div>
  )
}

export default UseContextHook

// context api is used to pass down the props inside the components.GLobal state for all of the components in the children.

