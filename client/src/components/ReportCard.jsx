import * as React from 'react';
import {Card, CardContent, CardActions, Button, Typography} from '@mui/material';
import styles from '../styles/ReportCard.module.css';

export default function ReportCard() {
    return (
        <Card className={styles.reportCard}>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    Анкета №_
                </Typography>
                <Typography variant="h5" component="div">
                    Фамилия Имя Отчество
                </Typography>
                <Typography color="text.secondary">
                    Год
                </Typography>
                <Typography>
                    Статус
                </Typography>
            </CardContent>
            <CardActions>
                <Button size="small">Открыть анкету</Button>
            </CardActions>
        </Card>
    );
}
