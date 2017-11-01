import { combineReducers } from 'redux';

// Reducers
import logReducer from './log-reducer';
import userReducer from './user-reducer';

// Combine Reducers
const reducers = combineReducers({
    LogState: logReducer,
    UserState: userReducer,
});

export default reducers;
