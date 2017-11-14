import React, {Component} from 'react'
import {logout} from "../../components/auth";
import {Redirect} from "react-router-dom";

class Logout extends Component {
    render() {
        logout();
        return (<Redirect to="/login/"/>);
    }
}

export default Logout;