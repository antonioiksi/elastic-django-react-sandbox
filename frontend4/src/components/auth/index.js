export const SESSION_JWTOKEN = 'SESSION_JWTOKEN';
export const SESSION_USER_INFO = 'SESSION_USER_INFO';

export const isAuth = () => {
    const jwt = sessionStorage.getItem(SESSION_JWTOKEN);
    if (!jwt)
        return false;
    else
        return true;
}

export const logout = () => {
    sessionStorage.removeItem(SESSION_JWTOKEN,null);
}

export const validToken = () => {
    const jwt = sessionStorage.getItem(SESSION_JWTOKEN);
    return  jwt;
}