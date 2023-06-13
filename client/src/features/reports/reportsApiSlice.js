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
            }),
            providesTags: ['Report'],
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
        getReportController: build.query({
            query: () => ({
                url: `/educator-report-controllers/me/`,
                method: 'GET'
            }),
            providesTags: ['ReportController'],
        }),
        changeReportStatus: build.mutation({
            query: ({ id, status }) => ({
                url: `/educator-reports/${id}/set_status/`,
                method: 'PATCH',
                body: { approved: status }
            }),
            invalidatesTags: ['Report', 'ReportList'],
        }),
        createReport: build.mutation({
            query: ({ educatorId, year }) => ({
                url: `/educator-reports/`,
                method: 'POST',
                body: { educator: educatorId, year, approved: false }
            }),
            invalidatesTags: ['ReportList'],
        }),
    })
})

export const {
    useGetMyReportsQuery,
    useGetReportQuery,
    useGetReportValuesQuery,
    usePatchReportValueMutation,
    useGetReportControllerQuery,
    useChangeReportStatusMutation,
    useCreateReportMutation,
} = reportsApiSlice
