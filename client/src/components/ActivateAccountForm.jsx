import * as React from "react";
import { Box, Button, Typography } from '@mui/material';
import styles from '../styles/Form.module.css';
import { useParams } from 'react-router-dom';
import { useActivateMutation } from '../features/auth/authApiSlice';
import { useNavigate } from 'react-router-dom'

export default function ActivateAccountForm() {
    let { uid, token } = useParams();
    const [activate] = useActivateMutation();
    const navigate = useNavigate();

    async function onSubmit(e) {
        try {
            let response = await activate({ uid, token });
            navigate('/login');     // TODO: sleep 1 sec with success message then navigate to login
            console.log(response);
        } catch (error) {
            console.log(error);    // TODO: add form message
        }
    }

    return (
        <Box className={ styles.formBoxContainer }>
            <Typography variant="h5" className={ styles.formTitle }>
                Подтвердите активацию
            </Typography>
            <Button onClick={ e => onSubmit(e) } variant="contained">Активировать</Button>
        </Box>
    );
}