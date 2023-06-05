import * as React from "react";
import { Box } from '@mui/material';
import Navbar from "../components/Navbar";
import SignupForm from "../components/SignupForm";
import styles from '../styles/Page.module.css';


export default function SignupPage() {
    return (
        <>
            <Navbar actions={[]} pageTitle={"Регистрация"} />
            <Box className={ `${styles.center} ${styles.pageTopMargin}` }>
                <SignupForm/>
            </Box>
        </>
    );
}