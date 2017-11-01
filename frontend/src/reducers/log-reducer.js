import * as types from '../actions/types';


const initialState = {
    fetching: false,
    logs: [],
    error: '',
    logsJWT: [],

};

const logReducer = function(state = initialState, action) {

    switch (action.type) {
        case types.LOGS_REQUEST:
            return { ...state, fetching: true };
        case types.LOGS_SUCCESS:
            return Object.assign({}, state, {logs: action.logs});
        case types.LOGS_FAILURE:
            return { ...state, fetching: true, error: action.error };
        case types.LOGS_JWT_REQUEST:
            return { ...state, fetching: true };
        case types.LOGS_JWT_SUCCESS:
            return Object.assign({}, state, {logsJWT: action.logs});
        case types.LOGS_JWT_FAILURE:
            return { ...state, fetching: true, error: action.error };
        default:
            break;
    }
    return state;

}

export default logReducer;
