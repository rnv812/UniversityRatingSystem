import * as React from 'react';
import {Box, TextField, Button, Typography} from '@mui/material';
import styles from '../styles/Form.module.css';
import { authorize } from '../API/auth';
import {Link} from "react-router-dom";


export default function LoginForm() {
    const [username, setUsername] = React.useState('');
    const [password, setPassword] = React.useState('');

    function submit() {
        authorize(username, password)
    }

    return (
        <Box className={styles['form-box-container']}>
            <Box className={styles['form-box']}>
                <Typography className={styles['form-title']} variant="h5" component="div">
                    Авторизация
                </Typography>
                <form>
                    <Box className={styles['form-field']}>
                        <TextField
                            style={{width: "370px"}}
                            value={username}
                            onChange={event => setUsername(event.target.value)}
                            label="Почта"
                            variant="outlined"
                        /> 
                    </Box>
                    <Box className={styles['form-field']}>
                        <TextField
                            style={{width: "370px"}}
                            value={password}
                            onChange={event => setPassword(event.target.value)}
                            label="Пароль"
                            variant="outlined"
                            type="password"
                        />
                    </Box>
                    <Box className={styles['submit-btn']}>
                        <Button style={{width: "370px"}} onClick={submit} variant="contained">Войти</Button>
                    </Box>
                </form>
                <Link to="/signup">
                    <Typography style={{marginTop: "20px"}}>
                        Создать аккаунт
                    </Typography>
                </Link>
            </Box>
        </Box>
    );
}