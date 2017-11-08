import React from 'react';
import { Redirect } from 'react-router';


export default class Logout extends React.Component {
    constructor(props) {
        super(props)

        sessionStorage.setItem('JWToken','');
    }



    render() {
        return (
            <Redirect to='/'/>
       )
    }
}