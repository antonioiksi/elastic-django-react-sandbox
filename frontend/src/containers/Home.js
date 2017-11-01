import React from 'react'

import { Redirect } from 'react-router'

import {Jumbotron, Button} from 'react-bootstrap'


export default class Home extends React.Component {

    state = {
        redirect: false
    }

    constructor(props, context) {
        super(props, context);

        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(event) {
        alert('Good luck!');
        //console.log('test');
        //this.context.router.history.push('/login');
        //this.context.router.transitionTo("/login");
        this.setState({redirect: true});
    }


    render() {

        const { redirect } = this.state;

        if (redirect)
            return <Redirect to='/login'/>;

        return (


            <div>
                <div className="container-fluid">
                    <div className="row">
                    <div className="col-lg-12">
                        <h1 className="page-header">reactapp</h1>
                        <Jumbotron>
                            <h1>Hello, world!</h1>
                            <p>This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
                            <p><Button bsStyle="primary" onClick={this.handleClick} >Let's start</Button></p>
                        </Jumbotron>
                    </div>
                </div>
            </div>
        </div>

        )
    }
}