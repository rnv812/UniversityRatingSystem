import React from 'react'
import { Box, Typography, Divider } from '@mui/material';
import { useParams } from 'react-router-dom';
import { useGetEducatorQuery } from '../features/educators/educatorsApiSlice';
import { useGetUserQuery } from '../features/auth/authApiSlice';
import { useGetReportValuesQuery } from '../features/reports/reportsApiSlice';
import ReportForm  from './ReportForm'; 


export default function ReportFormContainer({ report }) {
    const { id } = useParams();
    const { data: educator, isLoading: educatorLoading } = useGetEducatorQuery(report.educator);
    const { data: user, isLoading: userLoading } = useGetUserQuery(educator?.user, { skip: educatorLoading });
    const { data: reportValues } = useGetReportValuesQuery(id);

    return (
        <Box sx={{ width: "90%" }}>
            <Typography variant="h4">
                { userLoading 
                    ? 'Загрузка...'
                    : `${user?.last_name}  ${user?.first_name} ${user?.patronymic}, ${report?.year} год`
                }
            </Typography>
            <Divider />
            <ReportForm  reportValues={ reportValues } />
            
        </Box>
    )
}
