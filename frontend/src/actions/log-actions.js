import * as types from './types'
import axios from 'axios';
import store from "../store";




const URL = 'http://localhost:8000';



export function fetchLogsJWT() {
    return function action(dispatch) {
        dispatch({ type: types.LOGS_REQUEST })

        let token = sessionStorage.getItem('JWToken');
        const request = axios({
            method: 'GET',
            url: URL+'/api/log/all/',
            headers: {'Authorization':'Bearer '+token}
        });

        return request.then(
            response => dispatch(getLogsSuccess(response.data)),
            err => dispatch(getLogsFailure(err.message))
        );
    }
}

export function fetchLogs() {
    return function action(dispatch) {
        dispatch({ type: types.LOGS_REQUEST })

        const request = axios({
            method: 'GET',
            url: URL+'/api/elastic/hello_world/',
            headers: []
        });

        return request.then(
            response => dispatch(getLogsSuccess(response.data)),
            err => dispatch(getLogsFailure(err.message))
        );
    }
}






export function getLogs() {
  /*
  return {
    type: types.LOGS_SUCCESS,
    logs: [1,2,3,4,5]
  };
*/



  return (dispatch) => {
    dispatch({
      type: types.LOGS_REQUEST
    })


    setTimeout(() => {
      dispatch({
        type: types.LOGS_SUCCESS,
        logs: [1,2,3,4,5]
      })
    }, 1000)
  }

}

export function getLogsSuccess(logs) {
  return {
    type: types.LOGS_SUCCESS,
    logs
  };
}

export function getLogsFailure(error) {
  return {
    type: types.LOGS_FAILURE,
    error
  };
}