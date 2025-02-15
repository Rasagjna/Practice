import { combineReducers } from "redux";
import cakeReducer from "./cakes/cakeReducer";
import icecreamReducer from "./Icecream/IcecreamReducer";
import { user_reducer } from "./user/userReducer";

const rootReducer = combineReducers({
    cake:cakeReducer,
    icecream:icecreamReducer,
    user:user_reducer
})

export default rootReducer; 