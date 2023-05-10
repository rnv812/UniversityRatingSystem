import * as React from 'react';
import {Card, CardContent, CardActions, CardActionArea, Button, Typography} from '@mui/material';
import styles from '../styles/ReportCard.module.css';

export default function ReportCard() {
    return (
        <Card className={styles.reportCard}>
            <CardActionArea>
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
            </CardActionArea>
            <CardActions>
                <Button size="small">Открыть</Button>
                <Button size="small">Редактировать</Button>
                <Button size="small" color="error">Удалить</Button>
            </CardActions>
        </Card>
    );
}
