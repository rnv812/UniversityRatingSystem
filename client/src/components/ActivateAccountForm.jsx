import * as React from "react";
import {Box, Button, Typography} from '@mui/material';
import styles from '../styles/Form.module.css';


export default function ActivateAccountForm() {
    function submit() {

    }

    return (
        <Box className={styles['form-box-container']}>
            <Typography variant="h5" className={styles['form-title']}>
                Активация аккаунта
            </Typography>
            <Button onClick={submit} variant="contained">Активировать</Button>
        </Box>
    );
}