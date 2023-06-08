import { apiSlice } from "../../app/api/apiSlice";


export const authApiSlice = apiSlice.injectEndpoints({
    endpoints: build => ({
        login: build.mutation({
            query: credentials => ({
                url: '/jwt/create/',
                method: 'POST',
                body: { ...credentials }
            })
        }),
        signup: build.mutation({
            query: credentials => ({
                url: '/users/',
                method: 'POST',
                body: { ...credentials }
            })
        }),
        getUser: build.mutation({
            query: () => ({
                url: '/users/me/',
                method: 'GET'
            })
        }),
    })
})

export const { useLoginMutation, useSignupMutation, useGetUserMutation } = authApiSlice
