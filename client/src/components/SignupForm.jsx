import * as React from 'react';
import { Box, TextField, Button, Typography } from '@mui/material';
import { Link } from "react-router-dom";
import styles from '../styles/Form.module.css';
import { useSignupMutation } from '../features/auth/authApiSlice';


export default function SignupForm() {
    const [formData, setFormData] = React.useState({
        email: '',
        password: '',
        re_password: ''
    })
    const [signup] = useSignupMutation();

    const { email, password, re_password } = formData;

    function onChange(e) {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    }
    
    async function onSubmit(e) {
        e.preventDefault();
        try {
            let response = await signup(formData); // TODO: add form message "Check your email bruh"
            // it was sent to response.data.email
            setFormData({
                email: '',
                password: '',
                re_password: ''
            });
        } catch (error) {
            console.log(error.message);     // TODO: add form error message
        }
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
                            name="email"
                            value={ email }
                            onChange={ e => onChange(e) }
                            label="Почта"
                            variant="outlined"
                            sx={{ width: "100%" }}
                        /> 
                    </Box>
                    <Box className={ styles.formInput }>
                        <TextField
                            name="password"
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
                            name="re_password"
                            value={ re_password }
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