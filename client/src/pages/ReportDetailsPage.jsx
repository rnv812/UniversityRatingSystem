import * as React from "react";
import { useNavigate } from "react-router-dom";
import { Box } from "@mui/material"
import styles from "../styles/Page.module.css"
import ReportListNavbar from "../components/Navbar";
import ReportFormContainer from "../components/ReportFormContainer";

export default function ReportDetailsPage() {
    const navigate = useNavigate();
    
    function backToReports() {
        navigate('/reports')
    }

    let navbarActions = [
        {name: "Вернуться к анкетам", func: backToReports},
        {name: "Выйти", func: null}
    ]

    var fullname = "Фамилия Имя Отчество"

    return (
        <Box>
            <ReportListNavbar actions={navbarActions} pageTitle={fullname}/>
            <Box className={ `${styles.center} ${styles.pageTopStart}` }>
                <ReportFormContainer />
            </Box>
        </Box>
    );
}