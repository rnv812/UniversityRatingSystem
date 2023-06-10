import { apiSlice } from "../../app/api/apiSlice";


export const reportsApiSlice = apiSlice.injectEndpoints({
    endpoints: build => ({
        getMyReports: build.query({
            query: () => ({
                url: '/educator-reports/my/',
                method: 'GET'
            })
        }),
    })
})

export const {
    useGetMyReportsQuery,
} = reportsApiSlice
