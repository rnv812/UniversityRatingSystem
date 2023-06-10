import React from 'react'
import { Box, Typography, Divider } from '@mui/material';
import { useParams } from 'react-router-dom';
import { useGetReportQuery } from '../features/reports/reportsApiSlice';
import { useGetEducatorQuery } from '../features/educators/educatorsApiSlice';
import { useGetUserQuery } from '../features/auth/authApiSlice';
import { useGetReportValuesQuery } from '../features/reports/reportsApiSlice';

export default function ReportForm() {
    const { id } = useParams();
    const { data: report, isLoading: skipEducator } = useGetReportQuery(id);
    const { data: educator, isLoading: skipUser } = useGetEducatorQuery(report?.educator, { skip: skipEducator });
    const { data: user, isLoading } = useGetUserQuery(educator?.user, { skip: skipUser || skipEducator });
    const { data: reportValues } = useGetReportValuesQuery(id);

    return (
        <Box sx={{ width: "90%" }}>
            <Typography variant="h4">
                { isLoading 
                    ? 'Загрузка...'
                    : `${user?.last_name}  ${user?.first_name} ${user?.patronymic}, ${report?.year} год`
                }
            </Typography>
            <Divider />
            { JSON.stringify(reportValues) }
        </Box>
    )
}
