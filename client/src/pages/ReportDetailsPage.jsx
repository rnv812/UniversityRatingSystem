import * as React from "react";
import { useNavigate } from "react-router-dom";
import { Box } from "@mui/material"
import styles from "../styles/Page.module.css"
import ReportListNavbar from "../components/Navbar";
import ReportForm from "../components/ReportForm";

export default function ReportDetailsPage() {
    const navigate = useNavigate();
    
    function backToReports() {
        navigate('/reports')
    }

    const navbarActions = [
        {name: "Вернуться к анкетам", func: backToReports},
        {name: "Утвердить анкету", func: null},
        {name: "Редактировать анкету", func: null},
        {name: "Выйти", func: null}
    ]

    var fullname = "Фамилия Имя Отчество"

    return (
        <Box>
            <ReportListNavbar actions={navbarActions} pageTitle={fullname}/>
            <Box className={ `${styles.center} ${styles.pageTopStart}` }>
                <ReportForm />
            </Box>
        </Box>
    );
}