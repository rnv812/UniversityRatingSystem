import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    USER_LOAD_SUCCESS,
    USER_LOAD_FAIL,
    AUTHENTICATION_SUCCESS,
    AUTHENTICATION_FAIL,
    REFRESH_SUCCESS,
    REFRESH_FAIL,
    LOGOUT,
} from '../actions/types';


const initialState = {
    access: localStorage.getItem('access'),
    refresh: localStorage.getItem('refresh'),
    isAuthenticated: null,
    user: null
};


export default function auth(state = initialState, action) {
    const {type, payload} = action;

    switch(type) {
        case AUTHENTICATION_SUCCESS:
            return {
                ...state,
                isAuthenticated: true
            }
        case AUTHENTICATION_FAIL:
            return {
                ...state,
                isAuthenticated: false
            }
        case LOGIN_SUCCESS:
            localStorage.setItem('access', payload.access);
            localStorage.setItem('refresh', payload.access);
            return {
                ...state,
                isAuthenticated: true,
                access: payload.access,
                refresh: payload.refresh
            };
        case LOGIN_FAIL:
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            return {
                ...state,
                isAuthenticated: false,
                access: null,
                refresh: null,
                user: null
            };
        case LOGOUT:
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            return {
                ...state,
                isAuthenticated: false,
                access: null,
                refresh: null,
                user: null
            };
        case USER_LOAD_SUCCESS:
            return {
                ...state,
                user: payload
            };
        case USER_LOAD_FAIL:
            return {
                ...state,
                user: null
            };
        case REFRESH_SUCCESS:
            localStorage.setItem('access', payload.access);
            return {
                ...state,
                access: payload.access,
            };
        case REFRESH_FAIL:
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            return {
                ...state,
                isAuthenticated: false,
                access: null,
                refresh: null,
                user: null
            };
        default:
            return state;
    }
}