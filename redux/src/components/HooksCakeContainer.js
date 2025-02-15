import React from 'react'
import { buyCake } from '../redux'
import { useSelector,useDispatch } from 'react-redux'
function HookCakeContainer(){
    const numOfCakes = useSelector(state=> state.cake.numOfCakes)
const dispatch = useDispatch()
return (
    <div>
        <h2> Number of cakes - {numOfCakes}</h2>
        <button onClick={()=> dispatch(buyCake())}>Buy cakes </button>
    </div>
)
}

export default HookCakeContainer
//UseSelector acts as close equivalent to mapStateToProps function.