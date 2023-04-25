import * as React from 'react';
import {Box, TextField, Button, Typography} from '@mui/material';
import styles from '../styles/LoginForm.module.css';

export default function LoginForm() {
    return (
        <Box className={styles.formBox}>
            <Typography className={styles.formTitle} variant="h5" component="div">
                Авторизация
            </Typography>
            <form className={styles.form}>
                <TextField className={styles.formField} label="Имя пользователя" variant="outlined" />
                <TextField className={styles.formField} label="Пароль" variant="outlined" type="password"/>
                <Button className={styles.submitBtn} variant="contained">Войти</Button>
            </form>
        </Box>
    );
}