import React from 'react';
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux'

import * as logApi from '../../api/log-api'


import LogView from './log-view';

import * as logActions from '../../actions/log-actions'

class LogViewContainer extends React.Component {

    componentWillMount() {
        //logApi.apiGetLogs();
    }


    render() {
        const {fetching, logs, error} = this.props;
        const {fetchLogs, fetchLogsJWT} = this.props.logActions;
        return(
            <LogView fetching={false} logs={logs} error={error} getLogs={fetchLogs} getLogsJWT={fetchLogsJWT} />
        )
    }
}


const mapStateToProps = function(store) {
  return {
      fetching: store.LogState.fetching,
      logs: store.LogState.logs,
      error: store.LogState.error,
  };
};


const mapDispatchToProps = function(dispatch) {
  return {
    logActions: bindActionCreators(logActions, dispatch)
  };
};


export default connect(mapStateToProps,mapDispatchToProps)(LogViewContainer);
