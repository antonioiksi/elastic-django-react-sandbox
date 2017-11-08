import React from 'react';
import {Redirect} from 'react-router-dom';

import {isAuth} from "../";

export const AuthRequired = () => {
    return (
        isAuth() ? (<div>Authorized</div>) : (<Redirect to="/login"/>)
    )

}
