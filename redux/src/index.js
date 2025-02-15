import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import Main from './components/HooksTutorial/Main';
import UseEffectHook from './components/HooksTutorial/UseEffectHook';
import UseContextHook from './components/HooksTutorial/UseContextHook';
import UseReducerHook from './components/HooksTutorial/UseReducerHook';
import UseCallbackHook from './components/UseCallbackHook';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
    {/* <Main></Main> */}
    {/* <UseEffectHook></UseEffectHook> */}
    {/* <UseContextHook></UseContextHook> */}
    {/* <UseReducerHook></UseReducerHook> */}
    {/* <UseCallbackHook></UseCallbackHook> */}
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
