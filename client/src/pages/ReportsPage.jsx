import * as React from "react";
import {Box} from "@mui/material"
import Navbar from "../components/Navbar";
import ReportListContainer from "../components/ReportListContainer";
import CreateReportDialog from "../components/CreateReportDialog";


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

    return (
        <Box>
            <Navbar actions={[{name: "Создать анкету", func: handleClickOpenCreateReport}, {name: "Выйти", func: null}]} />
            <ReportListContainer reports={[{id: 1}, {id: 2}, {id: 3}]}/>
            <CreateReportDialog isOpen={isOpen} onClose={handleCloseCreateReport} onCreate={onCreateReport} />
        </Box>
    );
}