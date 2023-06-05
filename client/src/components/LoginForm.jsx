import * as React from 'react';
import { Box, TextField, Button, Typography } from '@mui/material';
import { Link } from "react-router-dom";
import styles from '../styles/Form.module.css';


export default function LoginForm() {
    const [formData, setFormData] = React.useState({
        email: '',
        password: ''
    })

    const { email, password } = formData;

    function onChange(e) {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    }
    
    function onSubmit(e) {
        e.preventDefault();
        // login(email, password)
    }

    return (
        <Box className={ styles.formBoxContainer }>
            <Typography variant="h5" className={ styles.formTitle }>
                Авторизация
            </Typography>
            <form>
                <Box className={ styles.formFields }>
                    <Box className={ styles.formInput }>
                        <TextField
                            value={ email }
                            name="email"
                            onChange={ e => onChange(e) }
                            label="Почта"
                            variant="outlined"
                            sx={{ width: "100%" }}
                        /> 
                    </Box>
                    <Box className={ styles.formInput }>
                        <TextField
                            value={ password }
                            name="password"
                            onChange={ e => onChange(e) }
                            label="Пароль"
                            variant="outlined"
                            type="password"
                            sx={{ width: "100%" }}
                        />
                    </Box>
                </Box>
                <Box className={ styles.formActions }>
                    <Link to="/signup" className={ styles.textAction }>
                        <Typography >
                            Нет аккаунта?
                        </Typography>
                    </Link>
                    <Button onClick={ e => onSubmit(e) } type="submit" variant="contained">Войти</Button>
                </Box>
            </form>
        </Box>
    );
}
