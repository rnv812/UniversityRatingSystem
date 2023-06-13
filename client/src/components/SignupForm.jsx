import { useState } from 'react';
import { Box, TextField, Button, Typography, FormHelperText } from '@mui/material';
import { Link } from "react-router-dom";
import styles from '../styles/Form.module.css';
import { useSignupMutation } from '../features/auth/authApiSlice';


export default function SignupForm() {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        re_password: ''
    });
    const [helperMessage, setHelperMessage] = useState("");
    const [errorStatus, setErrorStatus] = useState(false);
    const [emailError, setEmailError] = useState({ error: false, message: "" });
    const [passwordError, setPasswordError] = useState({ error: false, message: "" });
    const [repasswordError, setRepasswordError] = useState({ error: false, message: "" });
    const [registarionProcess, setRegistarionProcess] = useState(false);
    const [signup] = useSignupMutation();

    const { email, password, re_password } = formData;

    function onChange(e) {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    }
    
    async function onSubmit(e) {
        e.preventDefault();
        setErrorStatus(false);
        setHelperMessage('Регистрация...');
        setRegistarionProcess(true);
        setEmailError({ error: false, message: '' });
        setPasswordError({ error: false, message: '' });
        setRepasswordError({ error: false, message: '' });

        try {
            
            let response = await signup(formData);
            if (response?.error?.data) {
                let err_data = response?.error?.data;
                if ('email' in err_data) {
                    setEmailError({ error: true, message: err_data.email[0] });
                }

                if ('password' in err_data) {
                    setPasswordError({ error: true, message: err_data.password[0] });
                }

                if ('re_password' in err_data) {
                    setRepasswordError({ error: true, message: err_data.re_password[0] });
                }

                if ('non_field_errors' in err_data) {
                    setHelperMessage(err_data.non_field_errors[0]);
                }
                else {
                    setHelperMessage('');
                }
                
                setErrorStatus(true);
            }
            else {
                setHelperMessage('Письмо с подтверждением отправлено на указанную почту');
                setFormData({
                    email: '',
                    password: '',
                    re_password: ''
                });
            }
        } catch (error) {
            setErrorStatus(true);
            setHelperMessage('Ошибка регистрации');
        }

        setRegistarionProcess(false);
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
                            error={ emailError.error }
                            helperText={ emailError.message }
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
                            error={ passwordError.error }
                            helperText={ passwordError.message }
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
                            error={ repasswordError.error }
                            helperText={ repasswordError.message }
                            onChange={ e => onChange(e) }
                            label="Подтверждение пароля"
                            variant="outlined"
                            type="password"
                            sx={{ width: "100%" }}
                        />
                    </Box>
                    <FormHelperText error={ errorStatus }>{ helperMessage }</FormHelperText>
                </Box>
                <Box className={ styles.formActions }>
                    <Link to="/login" className={ styles.textAction }>
                        <Typography >
                            Уже есть аккаунт?
                        </Typography>
                    </Link>
                    <Button onClick={ e => onSubmit(e) } disabled={ registarionProcess }  variant="contained">Зарегистрироваться</Button>
                </Box>
            </form>
        </Box>
    );
}