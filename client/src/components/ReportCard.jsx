import * as React from 'react';
import { Button, Card, CardContent, CardActions, CardActionArea, Typography } from '@mui/material';
import styles from '../styles/ReportCard.module.css';
import { useGetEducatorQuery } from '../features/educators/educatorsApiSlice';
import { useGetUserQuery } from '../features/auth/authApiSlice';


export default function ReportCard({ report }) {
    const response =  useGetEducatorQuery(report.educator);
    const user = useGetUserQuery(response.data.user).data;

    return (
        <Card className={styles.reportCard}>
            <CardActionArea>
            <CardContent>
                <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                    {`Анкета №${report.id}` }
                </Typography>
                <Typography variant="h5" component="div">
                    { `${user.last_name}  ${user.first_name} ${user.patronymic}` }
                </Typography>
                <Typography color="text.secondary">
                    { `Год: ${report.year}` }
                </Typography>
                <Typography>
                    Статус: { 
                    report.approved 
                        ? <span style={{color: "green"}}>Подтверждена</span>
                        : <span style={{color: "chocolate"}}>На рассмотрении</span> 
                    }
                </Typography>
            </CardContent>
            </CardActionArea>
            <CardActions>
                <Button size="small">Открыть</Button>
                <Button size="small" color="error">Удалить</Button>
            </CardActions>
        </Card>
    );
}
