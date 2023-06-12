import * as React from "react";
import { useNavigate } from "react-router-dom";
import { Box } from "@mui/material"
import styles from "../styles/Page.module.css"
import ReportListNavbar from "../components/Navbar";
import ReportFormContainer from "../components/ReportFormContainer";
import { useSelector } from 'react-redux'
import { selectCurrentUser } from '../features/auth/authSlice'
import { useGetReportControllerQuery } from "../features/reports/reportsApiSlice";
import { useChangeReportStatusMutation } from "../features/reports/reportsApiSlice";
import { useParams } from 'react-router-dom';
import { useGetReportQuery } from '../features/reports/reportsApiSlice';


export default function ReportDetailsPage() {
    const navigate = useNavigate();
    const user = useSelector(selectCurrentUser);
    const { isLoading: controllerLoading, error: reportControllerError } = useGetReportControllerQuery();
    const [changeReportStatus] = useChangeReportStatusMutation();
    const { id } = useParams();
    const { data: report, isLoading: reportLoading } = useGetReportQuery(id);
    
    function backToReports() {
        navigate('/reports')
    }

    let navbarActions = [
        {name: "Вернуться к анкетам", func: backToReports},
        {name: "Выйти", func: null}
    ]

    if (!reportLoading && !controllerLoading && !reportControllerError) {
        const reportStatus = report.approved; 
        
        let changeStatusAction = {}; 

        if (reportStatus) {
            changeStatusAction = { 
                ...changeStatusAction,
                name: "Отменить утверждение",
                func: () => {changeReportStatus({ id, status: false })}
            }
        } else {
            changeStatusAction = { 
                ...changeStatusAction,
                name: "Утвердить анкету",
                func: () => {changeReportStatus({ id, status: true })}
            }
        }

        navbarActions.unshift(
            changeStatusAction
        )
    }

    return (
        <Box>
            <ReportListNavbar actions={navbarActions} pageTitle={ `${user.last_name}  ${user.first_name} ${user.patronymic}` } />
            <Box className={ `${styles.center} ${styles.pageTopStart}` }>
                { reportLoading 
                    ? "Загрузка..."
                    :  <ReportFormContainer report={ report }/>
                }
            </Box>
        </Box>
    );
}