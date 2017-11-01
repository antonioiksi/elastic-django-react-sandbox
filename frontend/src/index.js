import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import './index.css';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/css/bootstrap-theme.css';
import 'font-awesome/css/font-awesome.css';



import {BrowserRouter, Switch, Route} from 'react-router-dom'

import registerServiceWorker from './registerServiceWorker';

import store from './store';

import Home from './containers/Home';
import Login from './containers/Login';
import Dashboard from './containers/Dashboard';


ReactDOM.render(
    <Provider store={store}>
        <BrowserRouter>
            <Switch>
                <Route exact path='/' component={Home}/>
                <Route path='/login' component={Login}/>
                <Route path='/dashboard' component={Dashboard}/>
            </Switch>
        </BrowserRouter>
    </Provider>,
    document.getElementById('root')
);

registerServiceWorker();
