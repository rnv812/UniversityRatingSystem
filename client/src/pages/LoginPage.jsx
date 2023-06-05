import * as React from "react";
import { Box } from '@mui/material';
import { Navigate } from "react-router-dom";
import LoginForm from "../components/LoginForm";
import Navbar from "../components/Navbar";
import styles from '../styles/Page.module.css';


export default function LoginPage({isAuthenticated}) {
    if (false) {    // TODO: isAuthenticated
        return <Navigate to='/reports' />
    }

    return (
        <>
            <Navbar actions={[]} pageTitle={"Авторизация"} />
            <Box className={ `${styles.center} ${styles.pageTopMargin}` }>
                <LoginForm/>
            </Box>
        </>
    );
}
