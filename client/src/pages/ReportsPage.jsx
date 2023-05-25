import * as React from "react";
import {Box} from "@mui/material"
import Navbar from "../components/Navbar";
import ReportListContainer from "../components/ReportListContainer";
import CreateReportDialog from "../components/CreateReportDialog";
import Layout from "./Layout";


export default function ReportsPage() {
    const [isOpen, setOpenCreateReport] = React.useState(false);

    const handleClickOpenCreateReport = () => {
        setOpenCreateReport(true);
    };

    const handleCloseCreateReport = () => {
        setOpenCreateReport(false);
    };

    const onCreateReport = () => {
        // TODO send request to api
    };

    const navbarActions = [
        {name: "Создать анкету", func: handleClickOpenCreateReport},
        {name: "Выйти", func: null}
    ]

    var reports = [{id: 1}, {id: 2}, {id: 3}]

    const availableEducators = [{label: "Фамилия Имя Отчество", value: "TestName"}]
    const availableYears = [{label: "2023", value: "2023"}]


    return (
        <Layout>
            <Box>
                <Navbar actions={navbarActions} fullname={"Фамилия Имя Отчество"} />
                <ReportListContainer reports={reports}/>
                <CreateReportDialog 
                    isOpen={isOpen}
                    onClose={handleCloseCreateReport}
                    onCreate={onCreateReport} 
                    availableYears={availableYears}
                    availableEducators={availableEducators}
                />
            </Box>
        </Layout>
    );
}