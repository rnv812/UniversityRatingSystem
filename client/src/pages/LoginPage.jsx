import * as React from "react";
import {Box} from '@mui/material';
import LoginForm from "../components/LoginForm";
import styles from '../styles/Page.module.css';


export default function LoginPage() {
    return (
        <Box className={styles['page-center']}>
            <LoginForm/>
        </Box>
    );
}