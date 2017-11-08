import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import {PrivateRoute} from "./scenes/components/PrivateRoute";
import {AuthRoute} from "./scenes/components/AuthRoute";

import PropTypes from 'prop-types';


import {BrowserRouter, Switch, Route, Link, NavLink, Redirect} from 'react-router-dom';
import {Button} from 'react-bootstrap';

import {DashboardLayoutRoute} from './scenes/components/Header';

import Dashboard from './scenes/Dashboard';
import Search from './scenes/Search';

class Welcome extends React.Component {
    render() {
        return(
            <h1>Welcome public page</h1>
        )
    }
}

class Home extends React.Component {
    render() {
        return(
            <h1>Home public page</h1>
        )
    }
}

class Login extends Component {
    constructor(props) {
        super(props);

        this.state={Submited:false};
        this.handleClick = this.handleClick.bind(this);
    }


    handleClick(event) {
        localStorage.setItem('TOKEN_NAME', event.target.name);
        this.setState({Submited:true});
    }

    render() {
        let isLoggin = localStorage.getItem('TOKEN_NAME')!==''?(true):(false);
        let redirect = this.props.redirect;
        return (
            <div>
                <h1>Login page</h1>
                <Button name='aaa' onClick={this.handleClick}>Login</Button>
                <p>{redirect}</p>>
            {
                isLoggin?(<Redirect to="/dashboard"/>):('')
            }
            </div>
        )
    }
}

Login.propTypes = {
  redirect: PropTypes.string.isRequired,
};

const NoMatch = ({ location }) => (
  <div>
    <h3>No match for <code>{location.pathname}</code></h3>
  </div>
)

/*
ReactDOM.render(
    <BrowserRouter>
        <div>
            <ul>
                <li><Link to="/">Welcome (this is public)</Link></li>
                <li><Link to="/login">Login</Link></li>
                <li><NavLink to="/dashboard" activeClassName='hurray'>Dashboard</NavLink></li>
                <li><NavLink to="/search" activeClassName='hurray'>Search</NavLink></li>
            </ul>
            <hr/>

            <Switch>
                <Route exact path="/" component={Welcome}/>
                <Route exact path="/home" component={Home}/>
                <Route exact path="/login" component={Login}/>
                <PrivateRoute path="/dashboard" component={Dashboard}/>
                <DashboardLayoutRoute path="/search" component={Search}/>
                <Route component={NoMatch}/>
            </Switch>
        </div>
    </BrowserRouter>,
    document.getElementById('root'));
*/

ReactDOM.render(
    <BrowserRouter>
        <div>
            <ul>
                <li><Link to="/">Welcome (this is public)</Link></li>
                <li><Link to="/login">Login</Link></li>
                <li><NavLink to="/dashboard" activeClassName='hurray'>Private</NavLink></li>
            </ul>
            <hr/>
            <Switch>
                <Route exact path="/" component={Welcome}/>
                <Route exact path="/home" component={Home}/>
                <Route exact path="/login" component={Login} redirect="/dashboard"/>
                <AuthRoute exact path="/dashboard" component={Dashboard}/>
                <Route component={NoMatch}/>
            </Switch>
        </div>
    </BrowserRouter>,
    document.getElementById('root'));



registerServiceWorker();
