import React, {Component } from 'react'
import PropTypes from 'prop-types'

import {Button, Panel} from 'react-bootstrap'
import ReactJson from 'react-json-view'


export default class LogView extends Component {

    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this);
        this.handleClickJWT = this.handleClickJWT.bind(this);
    }


    handleClick(event) {
        this.props.getLogs();
    }

    handleClickJWT(event) {
        this.props.getLogsJWT();
    }

    render() {

        const wellStyles = {maxWidth: 400, margin: '0 auto 10px'};
        return (
            <div>
                <div className="well" style={wellStyles}>
                    <h1>LogView Component</h1>
                    <p>press button for loading...</p>
                    {
                        this.props.error!=='' ?
                            <Panel header="Error" bsStyle="danger">
                                {this.props.error}
                            </Panel>
                            :
                            ''
                    }
                    {
                        this.props.fetching ?
                            <Button bsStyle="primary" bsSize="large" block disabled >View logs</Button>
                            :
                            <Button bsStyle="primary" bsSize="large" block onClick={this.handleClick}>View logs</Button>
                    }
                    <Panel header="Logs" bsStyle="primary">
                        {JSON.stringify( this.props.logs)}
                    </Panel>
                    {
                        this.props.error===''?(<ReactJson src={this.props.logs} />):(<p>No result</p>)
                    }



                    <Button bsStyle="danger" bsSize="large" block onClick={this.handleClickJWT}>LOAD LOG (for authorized)</Button>
                </div>
            </div>
        )
    }
}

LogView.propTypes = {
    fetching: PropTypes.bool,
    logs: PropTypes.array,
    error: PropTypes.string,
    getLogs: PropTypes.func,
    getLogsJWT: PropTypes.func,
};
