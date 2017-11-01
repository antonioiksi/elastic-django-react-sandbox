import * as types from '../actions/types';


const initialState = {
    JWT: '',
};

const logReducer = function(state = initialState, action) {

    switch (action.type) {
        case types.JWT_LOGIN:
            return { ...state, JWT: action.jwt_token };
        case types.JWT_LOGOUT:
            return Object.assign({}, state, {JWT: ''});
        default:
            break;
    }
    return state;

}

export default logReducer;
