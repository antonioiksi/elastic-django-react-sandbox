import React, {Component} from 'react';
import { FormGroup, FormControl, ControlLabel, HelpBlock, Col, Button, Form, Panel } from 'react-bootstrap';
import { Redirect } from 'react-router';
import axios from 'axios';

import store from '../store';
import {userJWTLogin} from '../actions/user-actions'

export default class LoginForm extends Component {
  state = {
      username: '',
      password: '',
      redirect: false,
      error:'',
      validationState: {
          username: null,
          password: 'success',
      },
      submitDisabled: 'true',
  };

  constructor(props) {
    super(props);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    //this.primaryInput.focus();
  }

  handleChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    //alert(name+"-"+value);
    //alert([name]);

    this.setState({
      [name]: value
    });

    if(name==='username') {
        if (value.length === 0)
            this.setState({validationState: {username: null}});

        if (value.length < 5) {

            this.setState({validationState: {username: 'error'}},
                () => {
                    this.setState({submitDisabled: true});
                }
            );
        }
        else {
            this.setState({validationState: {username: 'success'}},
                function () {
                    //alert(this.state.validationState.username);
                    this.setState({submitDisabled: false});
                });
        }
    }


  }

    handleSubmit(event) {
      event.preventDefault();
      alert("usr:"+this.state.username+",pwd:"+this.state.password);

        const thiz = this;
      axios.post('http://localhost:8000/api/auth/token/obtain/', {
          username: this.state.username,
          password: this.state.password
      }).then(function (response) {
          console.log(response);

          sessionStorage.setItem('JWToken', response.data.access);

          store.dispatch(userJWTLogin(response.data.access));
          thiz.setState({redirect: true});
      }).catch(function (error) {
          console.log(error);
          thiz.setState({error: error.message});
      });
  }

  render() {

      const {username, password, redirect} = this.state;
      const validate_u = this.state.validationState.username;

      const submitDisabled = this.state.submitDisabled;

      if (redirect)
            return <Redirect to='/dashboard'/>;


    return (

        <Form horizontal onSubmit={this.handleSubmit}>
                    {
                        this.state.error!=='' ?
                            <Panel header="Error" bsStyle="danger">
                                {this.state.error}
                            </Panel>
                            :
                            ''
                    }

            <FormGroup controlId="formHorizontalLogin" validationState={validate_u}>
                <Col sm={12}>
                    <FormControl type="text"
                                 placeholder="username"
                                 name="username"
                                 value={username}
                                 onChange={this.handleChange}

                    />
                    <FormControl.Feedback/>
                </Col>
              <Col smOffset={4} sm={8}><HelpBlock>More than 2 symbols</HelpBlock></Col>
            </FormGroup>

            <FormGroup controlId="formHorizontalPassword">
                <Col componentClass={ControlLabel} sm={4}>Password</Col>
                <Col sm={8}>
                  <FormControl type="password" placeholder="password" name="password" value={password} onChange={this.handleChange} />
                </Col>
            </FormGroup>

            <FormGroup>
                <Col smOffset={0} sm={12}>
                  {submitDisabled ? (
                      <Button type="submit" bsStyle="success" block disabled>Sign in</Button>
                  ) : (
                      <Button type="submit" bsStyle="success" block>Sign in</Button>
                  )}
                </Col>
            </FormGroup>
        </Form>
    )
  }
}
