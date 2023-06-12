import { apiSlice } from "../../app/api/apiSlice";


export const authApiSlice = apiSlice.injectEndpoints({
    endpoints: build => ({
        login: build.mutation({
            query: credentials => ({
                url: '/jwt/create/',
                method: 'POST',
                body: { ...credentials }
            }),
            invalidatesTags: ['ReportList', 'ReportController'],
        }),
        signup: build.mutation({
            query: credentials => ({
                url: '/users/',
                method: 'POST',
                body: { ...credentials }
            })
        }),
        activate: build.mutation({
            query: obtainedPair => ({
                url: '/users/activation/',
                method: 'POST',
                body: { ...obtainedPair }
            })
        }),
        getUserMe: build.mutation({
            query: () => ({
                url: '/users/me/',
                method: 'GET'
            })
        }),
        getUser: build.query({
            query: (id) => ({
                url: `/users/${id}/`,
                method: 'GET'
            })
        })
    })
})

export const {
    useLoginMutation,
    useSignupMutation,
    useActivateMutation,
    useGetUserMeMutation,
    useGetUserQuery,
} = authApiSlice
