import * as React from 'react';
import {Container, Typography, Divider} from '@mui/material';
import ReportListFilter from './ReportListFilter';
import ReportList from './ReportList';
import styles from '../styles/ReportListContainer.module.css';


export default function ReportListContainer() {
    return (
        <Container className={styles.container}>
            <Typography variant="h4" component="div" sx={{ flexGrow: 1 }}>
                Список анкет
            </Typography>

            <ReportListFilter />

            <Divider />
            
            <ReportList reports={[{id: 1}, {id: 2}, {id: 3}]} />

        </Container>
    );
}