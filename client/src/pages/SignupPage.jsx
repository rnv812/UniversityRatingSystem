import * as React from "react";
import {Box} from '@mui/material';
import SignupForm from "../components/SignupForm";
import styles from '../styles/Page.module.css';
import Layout from "./Layout";


export default function SignupPage() {
    return (
        <Layout>
            <Box className={styles['page-center']}>
                <SignupForm/>
            </Box>
        </Layout>
    );
}