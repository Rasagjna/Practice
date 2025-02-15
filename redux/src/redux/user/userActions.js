import axios from "axios";
import { FETCH_USERS_FAILED, FETCH_USERS_REQUESTED, FETCH_USERS_SUCCEEDED } from "./userrTypes";

export const fetchUsersRequest = () => ({
    type:FETCH_USERS_REQUESTED
  });
  
 export const fetchUsersSuccess = users => ({
    type: FETCH_USERS_SUCCEEDED,
    payload: users
  });
  
 export  const fetchUsersFailure = error => ({
    type: FETCH_USERS_FAILED,
    payload: error
  });

export const fetchUsers = () =>{
    return (dispatch) =>{
        dispatch(fetchUsersRequest)
        axios.get('https://jsonplaceholder.typicode.com/users')
      .then(response => {
        // response.data is the users
        const users = response.data;
        dispatch(fetchUsersSuccess(users));
      })
      .catch(error => {
        // error.message is the error message
        dispatch(fetchUsersFailure(error.message));
      })

    }
}