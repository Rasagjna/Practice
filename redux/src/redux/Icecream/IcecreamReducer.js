import { BUY_ICECREAM } from "./IecreamType"

const initial_icecream_state = {
    num_of_icecreams: 20
}
const icecreamReducer = (state = initial_icecream_state,action) =>{
    switch(action.type){
        case BUY_ICECREAM:
            return {
                ...state,
                num_of_icecreams: state.num_of_icecreams-1
            }
        default: return state
    }
}
export default icecreamReducer