import React, {Component} from 'react'

import Form from './components/Form'
import {isAuth} from "../../components/auth";
import {Redirect} from "react-router-dom";

class Login extends Component {
    render() {
        //const jwt = sessionStorage.getItem(SESSION_JWTOKEN);
        //if(!jwt && jwt!=='')
        if(isAuth())
            return (<Redirect to="/dashboard/"/>)

        return (
            <div>
                <h1>Login</h1>
                <div><Form/></div>
            </div>
        )
    }
}

export default Login