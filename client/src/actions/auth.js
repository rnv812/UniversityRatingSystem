import axios from 'axios';
import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    USER_LOAD_SUCCESS,
    USER_LOAD_FAIL,
    AUTHENTICATION_SUCCESS,
    AUTHENTICATION_FAIL,
    LOGOUT
} from './types';

export const checkAuthenticated = () => async dispatch => {
    if (localStorage.getItem('access')) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        };

        const body = JSON.stringify({
            token: localStorage.getItem('access'),
        });

        try {
            const response = await axios.post(`${process.env.REACT_APP_API_URL}/jwt/verify`, body, config);
            if (response.data.code !== "token_not_valid") {
                dispatch({
                    type: AUTHENTICATION_SUCCESS
                });
            }
            else {
                dispatch({
                    type: AUTHENTICATION_FAIL
                });
            }
        } catch (err) {
            dispatch({
                type: AUTHENTICATION_FAIL
            });
        };
    }
    else {
        dispatch({
            type: AUTHENTICATION_FAIL
        });
    }
};

export const loadUser = () => async dispatch => {
    if (localStorage.getItem('access')) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`,
                'Accept': 'application/json'
            }
        };

        try {
            const response = await axios.get(`${process.env.REACT_APP_API_URL}/users/me`, config);
            dispatch({
                type: USER_LOAD_SUCCESS,
                payload: response.data
            });
        } catch (err) {
            dispatch({
                type: USER_LOAD_FAIL,
            });
        };
    }
    else {
        dispatch({
            type: USER_LOAD_FAIL,
        });
    }
};

export const login = (email, password) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
        }
    };

    const body = JSON.stringify({email, password});

    try {
        const response = await axios.post(`${process.env.REACT_APP_API_URL}/jwt/create`, body, config);

        dispatch({
            type: LOGIN_SUCCESS,
            payload: response.data
        });

        dispatch(loadUser());
    } catch (err) {
        dispatch({
            type: LOGIN_FAIL,
        });
    };
};

export const logout = () => dispatch => {
    dispatch({
        type: LOGOUT
    });
};