import React from 'react';
import ReactDOM from 'react-dom';
//import App from './App';
import registerServiceWorker from './registerServiceWorker';
import {BrowserRouter, Switch, Route, Link, Redirect} from 'react-router-dom'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/css/bootstrap-theme.css';
import 'font-awesome/css/font-awesome.css';

// react-bootstrap-table
import 'react-bootstrap-table/dist/react-bootstrap-table.min';
import 'react-bootstrap-table/dist/react-bootstrap-table.min.css';



import Welcome from './scenes/Welcome'
import Login from './scenes/Login'
import Dashboard from './scenes/Dashboard'
import Search from './scenes/Search'

import {EmptyRoute} from './components/layouts/EmptyRoute'
import {BackofficeRoute} from './components/layouts/BackofficeRoute'
import Logout from "./scenes/Logout";
import Test from "./scenes/Test";

//TODO add loading and keepeng auth token, don't forget abandon free access in DajngoServer

ReactDOM.render(
    <BrowserRouter>
        <div className="container-fluid">
            <ul>
                <li><Link to="/">Welcome</Link></li>
                <li><Link to="/login/">Login</Link></li>
                <li><Link to="/logout/">Logout</Link></li>
                <li><Link to="/test/">Test</Link></li>
            </ul>
            <hr/>
            <Switch>
                <Route exact path="/" component={Welcome}/>
                <EmptyRoute exact path="/login/" component={Login}/>
                <Route exact path="/test/" component={Test}/>
                <BackofficeRoute exact path="/logout/" component={Logout}/>
                <BackofficeRoute exact path="/dashboard/" component={Dashboard}/>
                <BackofficeRoute exact path="/search/" component={Search}/>
                <Route render={()=>(<Redirect to="/"/>)}/>
            </Switch>
        </div>
    </BrowserRouter>
    , document.getElementById('root'));
registerServiceWorker();
