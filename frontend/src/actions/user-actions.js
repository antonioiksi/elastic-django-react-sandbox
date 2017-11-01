import * as types from './types'


export function userJWTLogin(jwt_token) {
  return {
    type: types.JWT_LOGIN,
    jwt_token
  };
}

export function userJWTLogout() {
  return {
    type: types.JWT_LOGOUT
  };
}