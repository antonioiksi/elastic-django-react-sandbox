import React from 'react';
import {PrivateRoute} from "../PrivateRoute";
import { Route } from 'react-router-dom'
import { NavLink } from 'react-router-dom';


const Head = (
    <ul>
        <li><NavLink to="/dashboard" activeClassName='hurray'>Dashboard</NavLink></li>
        <li><NavLink to="/search" activeClassName='hurray'>Search</NavLink></li>
    </ul>
);



// wrapping/composing
export const DashboardLayoutRoute = ({ component: Component, ...rest }) => (
    <Route {...rest} render={props => (
        <div>
            <ul>
                <li><NavLink to="/dashboard" activeClassName='hurray'>Dashboard</NavLink></li>
                <li><NavLink to="/search" activeClassName='hurray'>Search</NavLink></li>
            </ul>
            <div>{this.props.children}</div>

        </div>
    )}/>
);