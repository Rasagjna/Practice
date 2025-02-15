import React from 'react'
import { buyCake } from '../redux'
import {connect} from 'react-redux'
function CakeContainer(props){
return (
    <div>
        <h2> Number of cakes - {props.numOfCakes}</h2>
        <button onClick={props.buyCake}>Buy cakes </button>
    </div>
)
}
// apart from whatever props cakeContainer is receiving, it will now receive additional prop - num of cakes.
const mapStateToProps = state =>{
    // returns object
    return {
        numOfCakes: state.numOfCakes
    }
}

// maps dispatch of an action creater to a prop in the component.
const mapDispatchToProps = dispatch => {
    return {
        buyCake:() => dispatch(buyCake())
    }
}

// connects component with store.
export default connect(mapStateToProps,mapDispatchToProps)(CakeContainer);
