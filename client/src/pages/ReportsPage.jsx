import * as React from "react";
import { Box } from "@mui/material"
import Navbar from "../components/Navbar";
import ReportListContainer from "../components/ReportListContainer";
import CreateReportDialog from "../components/CreateReportDialog";
import styles from "../styles/Page.module.css";
import { logout } from "../features/auth/authSlice";
import { useDispatch, useSelector } from 'react-redux'
import { selectCurrentUser } from '../features/auth/authSlice'



export default function ReportsPage() {
    const [isOpen, setOpenCreateReport] = React.useState(false);
    const dispatch = useDispatch();
    const user = useSelector(selectCurrentUser);

    const handleClickOpenCreateReport = () => {
        setOpenCreateReport(true);
    };

    const handleCloseCreateReport = () => {
        setOpenCreateReport(false);
    };

    const navbarActions = [
        { name: "Создать анкету", func: handleClickOpenCreateReport },
        { name: "Выйти", func: () => { dispatch(logout()) } }
    ]

    return (
        <>
            <Navbar actions={ navbarActions } pageTitle={ `${user.last_name}  ${user.first_name} ${user.patronymic}` } />
            <Box className={ `${styles.center} ${styles.pageTopStart}` }>
                <ReportListContainer/>
            </Box>
            <CreateReportDialog 
                isOpen={ isOpen }
                onClose={ handleCloseCreateReport }
            />
        </>
    );
}
