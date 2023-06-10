import { apiSlice } from "../../app/api/apiSlice";


export const reportsApiSlice = apiSlice.injectEndpoints({
    endpoints: build => ({
        getMyReports: build.query({
            query: () => ({
                url: '/educator-reports/my/',
                method: 'GET'
            })
        }),
        getReport: build.query({
            query: (id) => ({
                url: `/educator-reports/${id}/`,
                method: 'GET'
            })
        }),
        getReportValues: build.query({
            query: (id) => ({
                url: `/educator-indicator-values/${id}/report_values/`,
                method: 'GET'
            })
        }),
    })
})

export const {
    useGetMyReportsQuery,
    useGetReportQuery,
    useGetReportValuesQuery,
} = reportsApiSlice
