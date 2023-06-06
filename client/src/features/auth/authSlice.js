import { createSlice } from "@reduxjs/toolkit"


const authSlice = createSlice({
    name: 'auth',
    initialState: { user: null, access: null, refresh: null, isAuthenticated: false},
    reducers: {
        setCredentials: (state, action) => {
            const { access, refresh } = action.payload;
            state.access = access;
            state.refresh = refresh;
            state.isAuthenticated = true;

            localStorage.setItem('access', access);
            localStorage.setItem('refresh', refresh);
        },
        setUser: (state, action) => {
            state.user = action.payload;
        },
        logout: (state, _) => {
            state.user = null;
            state.access = null;
            state.refresh = null;
            state.isAuthenticated = false;

            state.access = localStorage.removeItem('access');
            state.refresh = localStorage.removeItem('refresh');
        },
        restoreSession: (state, _) => {
            let access = localStorage.getItem('access');
            let refresh = localStorage.getItem('refresh');
            state.isAuthenticated = access && refresh ? true : false;

            state.access = access
            state.refresh = refresh
        }
    },
})


export const { setCredentials, setUser, logout, restoreSession } = authSlice.actions

export default authSlice.reducer

export const selectCurrentUser = (state) => state.auth.user
export const selectCurrentToken = (state) => state.auth.access
export const selectIsAuthenticated = (state) => state.auth.isAuthenticated
