import * as React from "react";
import { Box, Button, Typography } from '@mui/material';
import styles from '../styles/Form.module.css';


export default function ActivateAccountForm() {
    function onSubmit() {

    }

    return (
        <Box className={ styles.formBoxContainer }>
            <Typography variant="h5" className={ styles.formTitle }>
                Подтвердите активацию
            </Typography>
            <Button onClick={ onSubmit() } variant="contained">Активировать</Button>
        </Box>
    );
}