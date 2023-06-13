import * as React from 'react';
import { Container, Typography, Divider } from '@mui/material';
import ReportListFilter from './ReportListFilter';
import ReportList from './ReportList';
import { useGetMyReportsQuery } from '../features/reports/reportsApiSlice';


export default function ReportListContainer() {
    const getMyReports = useGetMyReportsQuery();

    function getReports() {
        if (getMyReports?.data) {
            return getMyReports.data;
        } else {
            return [];
        }
    }
    
    let reports = getReports();

    return (
        <Container>
            <Typography variant="h4">
                Список анкет
            </Typography>
            <ReportListFilter />
            <Divider />
            <ReportList reports={ reports } />
        </Container>
    );
}