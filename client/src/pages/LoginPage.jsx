import * as React from "react";
import {Box} from '@mui/material';
import LoginForm from "../components/LoginForm";
import styles from '../styles/Page.module.css';
import Layout from "./Layout";


export default function LoginPage() {
    return (
        <Layout>
            <Box className={styles['page-center']}>
                <LoginForm/>
            </Box>
        </Layout>
    );
}