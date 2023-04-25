import * as React from "react";
import {Container} from "@mui/material"
import LoginForm from "../components/LoginForm";
import styles from '../styles/LoginForm.module.css';


export default function LoginPage() {
    return (
        <Container className={styles.formContainer}>
            <LoginForm/>
        </Container>
    );
}