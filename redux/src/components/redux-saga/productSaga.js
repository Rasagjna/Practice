// generator function - handle the async operations.
// return the result once operation is finished.
import {takeEvery,put} from 'redux-saga/effects'
import { PRODUCT_LIST, SET_PRODUCT_LIST } from './constants';

function* getProducts()
{
    console.warn("get product saga called")
    let data = yield fetch('https://jsonplaceholder.typicode.com/photos');
    data = yield data.json();
    console.warn("PRODUCT action is called",data)
    yield put({type: SET_PRODUCT_LIST,data})
}
function* productSaga()
{
    yield takeEvery(PRODUCT_LIST,getProducts)
}
export default productSaga;