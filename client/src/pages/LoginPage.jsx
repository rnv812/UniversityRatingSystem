import * as React from "react";
import { Box } from '@mui/material';
import LoginForm from "../components/LoginForm";
import Navbar from "../components/Navbar";
import styles from '../styles/Page.module.css';


export default function LoginPage() {
    return (
        <>
            <Navbar actions={[]} pageTitle={"Авторизация"} />
            <Box className={ `${styles.center} ${styles.pageTopMargin}` }>
                <LoginForm/>
            </Box>
        </>
    );
}
