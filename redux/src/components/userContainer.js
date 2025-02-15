import React from 'react'
import { connect } from 'react-redux'
import { useEffect } from 'react'
import { fetchUsers } from '../redux'

function UserContainer({users_data,fetchUsers}) {
    useEffect(()=>{
        fetchUsers();
            },[])
    return users_data.loading? 
    (<div>loading</div>): 
    users_data.error?
    (<h2> {users_data.error}</h2>):
    (<div>
        <h2> User list</h2>
        <div>
            {
                users_data && users_data.users && users_data.users.map(user => <p> {user.name}</p>)
            }
        </div>
    </div>)
  
}
const mapStateToProps = state =>{
    // returns object
    return {
        users_data: state.user
    }
}

// maps dispatch of an action creater to a prop in the component.
const mapDispatchToProps = dispatch => {
    return {
        fetchUsers:() => dispatch(fetchUsers())
    }
}

export default connect(mapStateToProps,mapDispatchToProps)(UserContainer)