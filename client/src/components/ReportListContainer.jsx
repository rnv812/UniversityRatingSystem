import * as React from 'react';
import { Container, Typography, Divider } from '@mui/material';
import ReportListFilter from './ReportListFilter';
import ReportList from './ReportList';


export default function ReportListContainer({reports}) {
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