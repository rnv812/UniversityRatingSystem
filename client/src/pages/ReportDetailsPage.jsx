import * as React from "react";
import { useNavigate } from "react-router-dom";
import { Box } from "@mui/material"
import ReportListNavbar from "../components/Navbar";
import Layout from "../layouts/Layout";


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
        <Layout>
            <Box>
                <ReportListNavbar actions={navbarActions} pageTitle={fullname}/>
            </Box>
        </Layout>
    );
}