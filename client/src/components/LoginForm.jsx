import * as React from 'react';
import {Box, TextField, Button, Typography} from '@mui/material';
import styles from '../styles/Form.module.css';
import { authorize } from '../API/auth';
import {Link} from "react-router-dom";


export default function LoginForm() {
    const [email, setEmail] = React.useState('');
    const [password, setPassword] = React.useState('');

    function submit() {
        authorize(email, password)
    }

    return (
        <Box className={styles['form-box-container']}>
            <Typography variant="h5" className={styles['form-title']}>
                Авторизация
            </Typography>
            <form>
                <Box className={styles['form-fields']}>
                    <Box className={styles['form-input']}>
                        <TextField
                            value={email}
                            onChange={event => setEmail(event.target.value)}
                            label="Почта"
                            variant="outlined"
                            sx={{width: "100%"}}
                        /> 
                    </Box>
                    <Box className={styles['form-input']}>
                        <TextField
                            value={password}
                            onChange={event => setPassword(event.target.value)}
                            label="Пароль"
                            variant="outlined"
                            type="password"
                            sx={{width: "100%"}}
                        />
                    </Box>
                </Box>
                <Box className={styles['form-actions']}>
                    <Link to="/signup" className={styles['text-action']}>
                        <Typography >
                            Нет аккаунта?
                        </Typography>
                    </Link>
                    <Button onClick={submit} variant="contained">Войти</Button>
                </Box>
            </form>
        </Box>
    );
}