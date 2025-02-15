import logo from './logo.svg';
import './App.css';
import CakeContainer from './components/CakeContainer';
import { Provider } from 'react-redux';
// import store from './redux/store';
import HookCakeContainer from './components/HooksCakeContainer';
import IcecremContainer from './components/IcecremContainer';
import NewCakeContainer from './components/newCakeContainer';
import UserContainer from './components/userContainer';
import store from './components/redux-saga/store';

import AddtoCartContainer from './components/Redux-Saga-Tutorial/AddtoCartContainer';
import { Header } from './components/Redux-Saga-Tutorial/Header';
function App() {
  return (
    <Provider store={store}>
      <div className="App">
     {/* <CakeContainer/> */}
     {/* <HookCakeContainer/>
     <IcecremContainer/>
     <NewCakeContainer/> */}
     {/* <UserContainer/> */}
     <Header></Header>
     <AddtoCartContainer></AddtoCartContainer>
  
    </div>
    </Provider>
   
    
  );
}

export default App;
