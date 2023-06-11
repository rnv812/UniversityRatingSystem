import { apiSlice } from "../../app/api/apiSlice";

export const reportsApiSlice = apiSlice.injectEndpoints({
    endpoints: build => ({
        getMyReports: build.query({
            query: () => ({
                url: '/educator-reports/my/',
                method: 'GET'
            }),
            providesTags: ['ReportList'],
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
            }),
            providesTags: ['ReportValues'],
        }),
        patchReportValue: build.mutation({
            query: ({ id, newValue }) => ({
                url: `/educator-indicator-values/${id}/`,
                method: 'PATCH',
                body: { value: newValue }
            }),
            invalidatesTags: ['ReportValues'],
        }),
    })
})

export const {
    useGetMyReportsQuery,
    useGetReportQuery,
    useGetReportValuesQuery,
    usePatchReportValueMutation,
} = reportsApiSlice
