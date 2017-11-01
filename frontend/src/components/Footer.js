import React from 'react'

import {Link} from 'react-router-dom'
import {ButtonToolbar, Button} from 'react-bootstrap'

export default class Footer extends React.Component {

    render(){
        return (
            <footer className='App-footer'>
                  <nav className="container">
                      <ButtonToolbar>
                          <Button bsStyle='link'><Link to='/'>Home</Link></Button>
                          <Button bsStyle='link'><Link to='/login'>Login</Link></Button>
                          <Button bsStyle='link'><Link to='/dashboard'>Dashboard</Link></Button>
                    </ButtonToolbar>
                </nav>
            </footer>
        )
    }
}