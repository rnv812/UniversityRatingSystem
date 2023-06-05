import * as React from "react";
import { Box } from '@mui/material';
import Navbar from "../components/Navbar";
import ActivateAccountForm from "../components/ActivateAccountForm";
import styles from '../styles/Page.module.css';


export default function ActivateAccountPage() {
    return (
        <>
            <Navbar actions={[]} pageTitle={"Активация аккаунта"} />
            <Box className={ `${styles.center} ${styles.pageTopMargin}` }>
                <ActivateAccountForm />
            </Box>
        </>
    );
}