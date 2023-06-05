import * as React from 'react';
import { Box, TextField, Button, Typography } from '@mui/material';
import { Link } from "react-router-dom";
import styles from '../styles/Form.module.css';


export default function SignupForm() {
    const [formData, setFormData] = React.useState({
        email: '',
        password: '',
        repassword: ''
    })

    const { email, password, repassword } = formData;

    function onChange(e) {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    }
    
    function onSubmit(e) {
        e.preventDefault();
        // signUp(email, password, repassword)
    }

    return (
        <Box className={ styles.formBoxContainer }>
            <Typography variant="h5" className={ styles.formTitle }>
                Регистрация
            </Typography>
            <form>
                <Box className={ styles.formFields }>
                    <Box className={ styles.formInput }>
                        <TextField
                            value={ email }
                            onChange={ e => onChange(e) }
                            label="Почта"
                            variant="outlined"
                            sx={{ width: "100%" }}
                        /> 
                    </Box>
                    <Box className={ styles.formInput }>
                        <TextField
                            value={ password }
                            onChange={ e => onChange(e) }
                            label="Пароль"
                            variant="outlined"
                            type="password"
                            sx={{ width: "100%" }}
                        />
                    </Box>
                    <Box className={ styles.formInput }>
                        <TextField
                            value={ repassword }
                            onChange={ e => onChange(e) }
                            label="Подтверждение пароля"
                            variant="outlined"
                            type="password"
                            sx={{ width: "100%" }}
                        />
                    </Box>
                </Box>
                <Box className={ styles.formActions }>
                    <Link to="/login" className={ styles.textAction }>
                        <Typography >
                            Уже есть аккаунт?
                        </Typography>
                    </Link>
                    <Button onClick={ e => onSubmit(e) } variant="contained">Зарегистрироваться</Button>
                </Box>
            </form>
        </Box>
    );
}