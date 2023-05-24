import * as React from "react";
import {Box, Button, Typography} from '@mui/material';
import styles from '../styles/LoginForm.module.css';

export default function ActivateAccountPage() {
    function submit() {
        
    }

    return (
        <Box className={styles['form-box-container']}>
            <Box className={styles['form-box']}>
                <Typography className={styles['form-title']} variant="h5" component="div">
                    Подтверждение аккаунта
                </Typography>
                <Box className={styles['submit-btn']}>
                        <Button style={{width: "370px"}} onClick={submit} variant="contained">Подтвердить</Button>
                </Box>
            </Box>
        </Box>
    );
}