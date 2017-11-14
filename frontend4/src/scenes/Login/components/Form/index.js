import React from 'react';
import {Redirect} from 'react-router-dom';

import {Form, FormGroup, Col, FormControl, ControlLabel, Checkbox, Button, Panel} from 'react-bootstrap';
import {obtain_jwt} from "../../../../services/auth";


class LoginForm extends React.Component {

    constructor(props) {
        super(props);


        this.state = {
            gotAccessToken:false,
            error:'',
            username:'',
            password:'',
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    handleChange(event) {
        const value = event.target.value;
        const name = event.target.name;
        this.setState({
            [name]: value
        });
    }

    handleSubmit(event) {
        event.preventDefault();
        obtain_jwt( this, this.state.username, this.state.password);
    }

    render() {

        const {username, password, error, gotAccessToken} = this.state;
        if(gotAccessToken) return (<Redirect to="/dashboard/"/>);

        return (


            <Form horizontal onSubmit={this.handleSubmit}>
                { error && <Panel header="Error" bsStyle="danger">{error}</Panel>}

                <FormGroup controlId="formHorizontalEmail">
                    <Col componentClass={ControlLabel} sm={2}>
                        Email
                    </Col>
                    <Col sm={10}>
                        <FormControl type="text"
                                     placeholder="username"
                                     onChange={this.handleChange}
                                     name="username"
                                     value={username}
                        />
                    </Col>
                </FormGroup>

                <FormGroup controlId="formHorizontalPassword">
                    <Col componentClass={ControlLabel} sm={2}>
                        Password
                    </Col>
                    <Col sm={10}>
                        <FormControl type="password" placeholder="password" name="password" value={password} onChange={this.handleChange} />
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