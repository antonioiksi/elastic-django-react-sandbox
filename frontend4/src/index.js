import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import {BrowserRouter, Switch, Route, Link, Redirect} from 'react-router-dom'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/css/bootstrap-theme.css';
import 'font-awesome/css/font-awesome.css';


import Welcome from './scenes/Welcome'
import Login from './scenes/Login'
import Dashboard from './scenes/Dashboard'
import Search from './scenes/Search'

import {EmptyRoute} from './components/layouts/EmptyRoute'
import {BackofficeRoute} from './components/layouts/BackofficeRoute'

//TODO add loading and keepeng auth token, don't forget abandon free access in DajngoServer

ReactDOM.render(
    <BrowserRouter>
        <div className="container-fluid">
            <ul>
                <li><Link to="/">Welcome</Link></li>
                <li><Link to="/login/">Login</Link></li>
            </ul>
            <hr/>
            <Switch>
                <Route exact path="/" component={Welcome}/>
                <EmptyRoute exact path="/login/" component={Login}/>
                <BackofficeRoute exact path="/dashboard/" component={Dashboard}/>
                <BackofficeRoute exact path="/search/" component={Search}/>
                <Route render={()=>(<Redirect to="/"/>)}/>
            </Switch>
        </div>
    </BrowserRouter>
    , document.getElementById('root'));
registerServiceWorker();
