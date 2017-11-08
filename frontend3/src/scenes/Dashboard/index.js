import React from 'react';
import {Button} from 'react-bootstrap';


export default class Dashboard extends React.Component {

    static isPrivate = true;

    constructor(props){
        super(props);

        this.handleClickLogout = this.handleClickLogout.bind(this);
    }

    handleClickLogout(event) {
        localStorage.setItem('TOKEN_NAME','');
        this.props.history.push('/login');
    }

    render(){
        return (
            <div>
                <h1>Dashboard page</h1>
                <Button name='LogoutButton' onClick={this.handleClickLogout}>LogOut</Button>
            </div>);
    }
}
