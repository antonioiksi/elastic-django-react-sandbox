import React from 'react';
import {Redirect} from 'react-router-dom';

import {Form, FormGroup, Col, FormControl, ControlLabel, Checkbox, Button} from 'react-bootstrap';


class LoginForm extends React.Component {

    constructor(props) {
        super(props);

        this.state = {isLoggedIn:false};
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleSubmit(event) {
        alert(event.target.name);
        this.setState({isLoggedIn:true});
    }

    render() {

        if(this.state.isLoggedIn) return (<Redirect to="/dashboard/"/>);

        return (


            <Form horizontal>
                <FormGroup controlId="formHorizontalEmail">
                    <Col componentClass={ControlLabel} sm={2}>
                        Email
                    </Col>
                    <Col sm={10}>
                        <FormControl type="text" placeholder="User" />
                    </Col>
                </FormGroup>

                <FormGroup controlId="formHorizontalPassword">
                    <Col componentClass={ControlLabel} sm={2}>
                        Password
                    </Col>
                    <Col sm={10}>
                        <FormControl type="password" placeholder="Password" />
                    </Col>
                </FormGroup>

                <FormGroup>
                    <Col smOffset={2} sm={10}>
                        <Checkbox>Remember me</Checkbox>
                    </Col>
                </FormGroup>

                <FormGroup>
                    <Col smOffset={2} sm={10}>
                        <Button type="submit" name="Hi" onClick={this.handleSubmit}>
                            Sign in
                        </Button>
                    </Col>
                </FormGroup>
            </Form>
        )
    }
}


export default LoginForm;