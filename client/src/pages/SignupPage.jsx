import * as React from "react";
import {Box} from '@mui/material';
import SignupForm from "../components/SignupForm";
import styles from '../styles/Page.module.css';


export default function SignupPage() {
    return (
        <Box className={styles['page-center']}>
            <SignupForm/>
        </Box>
    );
}