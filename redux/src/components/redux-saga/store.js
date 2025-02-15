import {createStore} from 'redux'
import rootReducer from './rootReducer';
import { configureStore } from '@reduxjs/toolkit';
import productSaga from './productSaga';
import createSagaMiddleware from 'redux-saga';

// const dummyReducer = () =>{
//     return 100;
// }

// const store = createStore(rootReducer);
const sagaMiddleware = createSagaMiddleware();
const store = configureStore({
    reducer:rootReducer,
    middleware:()=>[sagaMiddleware]
})

sagaMiddleware.run(productSaga);
export default store;