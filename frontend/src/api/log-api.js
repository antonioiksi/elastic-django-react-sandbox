import axios from 'axios';
import store from '../store';
import {getLogsFailure, getLogsSuccess} from '../actions/log-actions';
import * as types from '../actions/types';

const URL = 'http://localhost:8000';




/**
 * Get all logs
 */
export function apiGetLogs() {

    let url = URL+'/api/elastic/hello_world/';

    return axios.get(url)
        .then(response => {
            console.log(response.data);
            const jsonData = [ "Ford", "BMW", "Fiat" ];// JSON.stringify( response.data);

            return {
                type: types.LOGS_SUCCESS,
                logs: jsonData
            }
        })
        .catch(error => {
            console.log(error);
            return {
                type: types.LOGS_FAILURE,
                error: error.message
            }
        });
}

export function apiGetLogs2() {
    return axios.get(URL+'/api/elastic/hello_world/')
        .then(response => {
            console.log(response);
            store.dispatch(getLogsSuccess(response.data));
            return response;
        })
        .catch(error => {
            console.log(error);
            store.dispatch(getLogsFailure(error.message));
            return '[]';
        });
}

