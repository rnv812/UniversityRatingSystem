import * as React from 'react';
import {Container, Typography, Divider} from '@mui/material';
import ReportListFilter from './ReportListFilter';
import ReportList from './ReportList';
import styles from '../styles/ReportListContainer.module.css';


export default function ReportListContainer({reports}) {
    return (
        <Container className={styles.container}>
            <Typography variant="h4">
                Список анкет
            </Typography>

            <ReportListFilter />

            <Divider />
            
            <ReportList reports={reports} />

        </Container>
    );
}