import * as React from "react";
import { useNavigate } from "react-router-dom";
import { Box } from "@mui/material"
import styles from "../styles/Page.module.css"
import ReportListNavbar from "../components/Navbar";
import ReportFormContainer from "../components/ReportFormContainer";
import { useSelector } from 'react-redux'
import { selectCurrentUser } from '../features/auth/authSlice'


export default function ReportDetailsPage() {
    const navigate = useNavigate();
    const user = useSelector(selectCurrentUser);
    
    function backToReports() {
        navigate('/reports')
    }

    let navbarActions = [
        {name: "Вернуться к анкетам", func: backToReports},
        {name: "Выйти", func: null}
    ]

    return (
        <Box>
            <ReportListNavbar actions={navbarActions} pageTitle={ `${user.last_name}  ${user.first_name} ${user.patronymic}` } />
            <Box className={ `${styles.center} ${styles.pageTopStart}` }>
                <ReportFormContainer />
            </Box>
        </Box>
    );
}