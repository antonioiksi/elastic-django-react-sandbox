import React from 'react';
import { Route, Redirect} from 'react-router-dom'
import PropTypes from 'prop-types'

import {DashboardLayoutRoute} from "../Header";

export const PrivateRoute = ({ component: Component, ...rest }) => (
    <Route {...rest} render={props => (
        localStorage.getItem('TOKEN_NAME')!=='' ? (
            <DashboardLayoutRoute>
                <Component {...props}/>
            </DashboardLayoutRoute>
        ) : (
            <Redirect to={{
                pathname: '/login',
                state: { from: props.location }
            }}/>
        )
    )}/>
);


