import React,{useState} from 'react'
import { buyCake } from '../redux'
import {connect} from 'react-redux'
function NewCakeContainer(props){
    const [number,setNumber] = useState(1)
return (
    <div>
        <h2> Number of cakes - {props.numOfCakes}</h2>
        <input type= 'text' value = {number} onChange={e=>setNumber(e.target.value)}/>
        <button onClick={() => props.buyCake(number)}>Buy {number} cakes </button>
    </div>
)
}
// apart from whatever props cakeContainer is receiving, it will now receive additional prop - num of cakes.
// apart from state, we can also pass ownProps as other argument to mapStateToProps. Props that we pass to fuction
const mapStateToProps = state =>{
    // returns object
    return {
        numOfCakes: state.cake.numOfCakes
    }
}

// maps dispatch of an action creater to a prop in the component.
const mapDispatchToProps = dispatch => {
    return {
        buyCake:(number) => dispatch(buyCake(number))
    }
}

// connects component with store.
export default connect(mapStateToProps,mapDispatchToProps)(NewCakeContainer);
