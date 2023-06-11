import { apiSlice } from "../../app/api/apiSlice";


export const ratingApiSlice = apiSlice.injectEndpoints({
    endpoints: build => ({
        getIndicators: build.query({
            query: () => ({
                url: '/indicators/',
                method: 'GET'
            })
        }),
    })
})

export const {
    useGetIndicatorsQuery,
} = ratingApiSlice
