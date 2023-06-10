import { useEffect, useState } from 'react'
import { Box, TextField, Button, Typography, FormHelperText } from '@mui/material';
import { Link } from "react-router-dom";
import styles from '../styles/Form.module.css';
import { useDispatch, useSelector } from 'react-redux'
import { useLoginMutation, useGetUserMutation } from '../features/auth/authApiSlice';
import { useNavigate } from 'react-router-dom'
import { setCredentials, setUser, restoreSession, selectIsAuthenticated } from '../features/auth/authSlice'


export default function LoginForm() {
    const [formData, setFormData] = useState({ email: '', password: '' })
    const [helperMessage, setHelperMessage] = useState("")
    const [errorStatus, setErrorStatus] = useState(false)
    const dispatch = useDispatch();
    const [login] = useLoginMutation();
    const [getUser] = useGetUserMutation();
    const navigate = useNavigate();
    const isAuthenticated = useSelector(selectIsAuthenticated);

    const { email, password } = formData;

    function onChange(e) {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    }

    useEffect(() => {
        async function fetchUser() {
            dispatch(restoreSession());
            if (isAuthenticated) {
                try {
                    const user = await getUser().unwrap();
                    dispatch(setUser(user));
                    navigate('/reports')
                } catch (error) {
                    setHelperMessage("Сессия истекла");
                }
            }
        }
        fetchUser();
    }, [dispatch, getUser, navigate, isAuthenticated]);

    async function onSubmit(e) {
        e.preventDefault();
        
        try {
            setErrorStatus(false);
            setHelperMessage("Авторизация...");
            const credentials = await login({ email, password }).unwrap();
            dispatch(setCredentials(credentials));
            const user = await getUser().unwrap();
            dispatch(setUser(user));
            setFormData({
                email: '',
                password: ''
            });
            navigate('/reports')
            
        } catch (error) {
            setErrorStatus(true);
            if (error.status === 401) {
                setHelperMessage("Неверные учётные данные или аккаунт не активирован");
            }
            else {
                setHelperMessage("Сервер недоступен");
            }
        }
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
                    <FormHelperText error={ errorStatus }>{ helperMessage }</FormHelperText>
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
