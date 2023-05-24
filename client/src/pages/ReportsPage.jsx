import * as React from "react";
import {
    Button,
    Box,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
} from "@mui/material"
import Navbar from "../components/Navbar";
import ReportListContainer from "../components/ReportListContainer";
import ItemSelect from '../components/ItemSelect';


export default function ReportsPage() {
    const [open, setOpen] = React.useState(false);

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };

    return (
        <Box>
            <Navbar actions={[{name: "Создать анкету", func: handleClickOpen}, {name: "Выйти", func: null}]} />
            <ReportListContainer reports={[{id: 1}, {id: 2}, {id: 3}]}/>
            <Dialog
                open={open}
                keepMounted
                onClose={handleClose}
                aria-describedby="alert-dialog-slide-description"
            >
                <DialogTitle>{"Создание анкеты"}</DialogTitle>
                <DialogContent>
                    <Box style={{display:"flex", flexDirection: "column"}}>
                        <ItemSelect
                            id={'report-educator'}
                            title={"Преподаватель"}
                            items={[{label: "Фамилия Имя Отчество", value: "TestName"}]}
                            defaultValue={"TestName"}
                            sx={{ minWidth: "340px", marginTop: "20px" }}
                        />
                        <ItemSelect
                            id={'report-year'}
                            title={"Год анкеты"}
                            items={[{label: "2023", value: "2022"}]}
                            defaultValue={"2023"}
                            sx={{ minWidth: "340px", marginTop: "20px"}}
                        />
                    </Box>
                </DialogContent>
                <DialogActions>
                <Button onClick={handleClose}>Создать</Button>
                <Button onClick={handleClose}>Отменить</Button>
                </DialogActions>
            </Dialog>
        </Box>
    );
}