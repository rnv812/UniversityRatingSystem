import * as React from 'react';
import { connect } from 'react-redux';
import {Box, TextField, Button, Typography} from '@mui/material';
import styles from '../styles/Form.module.css';
import {Link} from "react-router-dom";
import { login } from '../actions/auth';


function LoginForm({login}) {
    const [formData, setFormData] = React.useState({
        email: '',
        password: ''
    })

    const {email, password} = formData;

    function onChange(e) {
        setFormData({...formData, [e.target.name]: e.target.value});
    }
    
    function onSubmit(e) {
        e.preventDefault();
        login(email, password)
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
                            name="email"
                            onChange={e => onChange(e)}
                            label="Почта"
                            variant="outlined"
                            sx={{width: "100%"}}
                        /> 
                    </Box>
                    <Box className={styles['form-input']}>
                        <TextField
                            value={password}
                            name="password"
                            onChange={e => onChange(e)}
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
                    <Button onClick={e=> onSubmit(e)} type="submit" variant="contained">Войти</Button>
                </Box>
            </form>
        </Box>
    );
}

// const mapStateToProps = state => ({
//     //TODO implement auth check

// });

export default connect(null, { login })(LoginForm);
