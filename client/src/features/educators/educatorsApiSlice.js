import { apiSlice } from "../../app/api/apiSlice";


export const educatorsApiSlice = apiSlice.injectEndpoints({
    endpoints: build => ({
        getEducator: build.query({
            query: (id) => ({
                url: `/educators/${id}/`,
                method: 'GET'
            })
        }),
        getEducatorMe: build.query({
            query: () => ({
                url: `/educators/me/`,
                method: 'GET'
            })
        }),
    })
})

export const {
    useGetEducatorQuery,
    useGetEducatorMeQuery,
} = educatorsApiSlice
