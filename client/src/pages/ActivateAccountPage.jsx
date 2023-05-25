import * as React from "react";
import {Box} from '@mui/material';
import ActivateAccountForm from "../components/ActivateAccountForm";
import styles from '../styles/Page.module.css';
import Layout from "./Layout";

export default function ActivateAccountPage() {
    return (
        <Layout>
            <Box className={styles['page-center']}>
                <ActivateAccountForm />
            </Box>
        </Layout>
    );
}