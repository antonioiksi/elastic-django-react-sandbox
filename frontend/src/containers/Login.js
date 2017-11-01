import React from 'react';
import LoginForm from "../components/LoginForm";


export default class Home extends React.Component {

    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-4 col-md-offset-4">
                        <div className="login-panel panel panel-default">
                            <div className="panel-heading">
                                <h3 className="panel-title">Please Sign In</h3>
                            </div>
                            <div className="panel-body">
                                <LoginForm/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
