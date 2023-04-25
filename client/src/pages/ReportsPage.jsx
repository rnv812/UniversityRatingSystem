import * as React from "react";
import {Box} from "@mui/material"
import ReportListNavbar from "../components/ReportListNavbar";
import ReportListContainer from "../components/ReportListContainer";


export default function ReportsPage() {
    return (
        <Box>
            <ReportListNavbar/>
            <ReportListContainer/>
        </Box>
    );
}