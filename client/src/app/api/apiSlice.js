import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { setCredentials, logout } from '../../features/auth/authSlice';


const baseQuery = fetchBaseQuery({
    baseUrl: process.env.REACT_APP_API_URL,
    prepareHeaders: (headers, { getState }) => {
        const token = getState().auth.access
        if (token) {
            headers.set('Authorization', `JWT ${token}`);
        }
        return headers;
    }
});


// wrapper for baseQuery (refreshes the access token on expiration)
const baseQueryReauth = async (args, api, extraOptions) => {
    let result = await baseQuery(args, api, extraOptions);

    if (result?.error?.status === 401 && api.getState().auth.refresh) {
        const refreshResult = await baseQuery(
            {
                url: '/jwt/refresh',
                method: 'POST',
                body: { refresh: api.getState().auth.refresh }
            },
            api,
            extraOptions
        );

        console.log('Refresh result: ', refreshResult);
        if (refreshResult?.data) {
            const refresh = api.getState().auth.refresh;
            console.log('Here is new access received from api');
            const access = refreshResult.data.access;
            api.dispatch(setCredentials({ refresh, access }));
            result = await baseQuery(args, api, extraOptions);
        } else {
            api.dispatch(logout());
        }
    }

    return result;
}

export const apiSlice = createApi({
    baseQuery: baseQueryReauth,
    endpoints: build => ({})
});