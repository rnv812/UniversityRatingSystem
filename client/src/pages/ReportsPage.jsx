import * as React from "react";
import {Box} from "@mui/material"
import Navbar from "../components/Navbar";
import ReportListContainer from "../components/ReportListContainer";


export default function ReportsPage() {
    return (
        <Box>
            <Navbar actions={[{name: "Создать анкету", func: null}, {name: "Выйти", func: null}]} />
            <ReportListContainer reports={[{id: 1}, {id: 2}, {id: 3}]}/>
        </Box>
    );
}