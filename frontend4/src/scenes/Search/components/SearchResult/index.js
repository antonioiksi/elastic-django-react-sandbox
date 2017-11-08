import React from 'react'
import PropTypes from 'prop-types'
import ReactJson from 'react-json-view'
import {Panel} from "react-bootstrap";

class SearchResult extends React.Component {

    render() {
        return (
            <div>
                <h1>Search Result</h1>
                        <Panel header="Результат" bsStyle="info">
                            <ReactJson src={this.props.jsonData} />
                        </Panel>
            </div>
        )
    }

}

SearchResult.PropTypes = {
    jsonData: PropTypes.array,
};

export default SearchResult;