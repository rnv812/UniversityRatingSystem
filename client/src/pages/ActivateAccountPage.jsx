import * as React from "react";
import {Box} from '@mui/material';
import ActivateAccountForm from "../components/ActivateAccountForm";
import styles from '../styles/Page.module.css';


export default function ActivateAccountPage() {
    return (
        <Box className={styles['page-center']}>
            <ActivateAccountForm />
        </Box>
    );
}