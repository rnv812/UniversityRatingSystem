import * as React from 'react';
import { Box, Typography } from '@mui/material';
import ReportCard from './ReportCard';
import styles from '../styles/ReportList.module.css';


export default function ReportList({reports}) {
    return (
        <Box className={ styles.reportList }>
            {
                reports.length
                ? reports.map(report => <ReportCard key={ report.id } report={ report } />)
                : <Typography align='center' variant="h5" color="text.secondary">Список пуст</Typography>
            }
        </Box>
    );
}