import { createStore,applyMiddleware } from "redux";
import cakeReducer from "./cakes/cakeReducer";
import { composeWithDevTools } from 'redux-devtools-extension';
import { thunk } from "redux-thunk";
import logger from "redux-logger";
import rootReducer from "./rootReducer";
const store = createStore(rootReducer,composeWithDevTools(applyMiddleware(logger,thunk)))
export default store