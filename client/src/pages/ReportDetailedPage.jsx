import * as React from "react";
import {Box} from "@mui/material"
import ReportListNavbar from "../components/Navbar";


export default function ReportDetailedPage() {
    return (
        <Box>
            <ReportListNavbar actions={[{name: "Вернуться к анкетам", func: null}, {name: "Утвердить анкету", func: null}, {name: "Редактировать анкету", func: null}, {name: "Выйти", func: null}]}/>
            
        </Box>
    );
}