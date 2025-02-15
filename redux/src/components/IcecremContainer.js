import React from 'react'
import { buy_icecream } from '../redux'
import {connect} from 'react-redux'
function IcecreamContainer(props){
return (
    <div>
        <h2> Number of icecreams - {props.numOfIcecreams}</h2>
        <button onClick={props.buy_icecream}>Buy icecreams </button>
    </div>
)
}
// apart from whatever props cakeContainer is receiving, it will now receive additional prop - num of cakes.
const mapStateToProps = state =>{
    // returns object
    return {
        numOfIcecreams:state.icecream.num_of_icecreams
    }
}

// maps dispatch of an action creater to a prop in the component.
const mapDispatchToProps = dispatch => {
    return {
        buy_icecream:() => dispatch(buy_icecream())
    }
}

// connects component with store.
export default connect(mapStateToProps,mapDispatchToProps)(IcecreamContainer);
