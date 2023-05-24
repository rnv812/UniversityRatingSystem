import * as React from 'react';
import {Box, TextField, Button, Typography} from '@mui/material';
import styles from '../styles/Form.module.css';
import { authorize } from '../API/auth';
import {Link} from "react-router-dom";


export default function SignupForm() {
    const [email, setEmail] = React.useState('');
    const [password, setPassword] = React.useState('');
    const [repassword, setRepassword] = React.useState('');

    function submit() {
        authorize(email, password)
    }

    return (
        <Box className={styles['form-box-container']}>
            <Typography variant="h5" className={styles['form-title']}>
                Регистрация
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
                    <Box className={styles['form-input']}>
                        <TextField
                            value={repassword}
                            onChange={event => setRepassword(event.target.value)}
                            label="Подтверждение пароля"
                            variant="outlined"
                            type="password"
                            sx={{width: "100%"}}
                        />
                    </Box>
                </Box>
                <Box className={styles['form-actions']}>
                    <Link to="/login" className={styles['text-action']}>
                        <Typography >
                            Уже есть аккаунт?
                        </Typography>
                    </Link>
                    <Button onClick={submit} variant="contained">Зарегистрироваться</Button>

                </Box>
            </form>
        </Box>
    );
}