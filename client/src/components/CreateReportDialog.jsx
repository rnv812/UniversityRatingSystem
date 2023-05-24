import * as React from "react";
import {
    Button,
    Box,
    Dialog,
    DialogActions,
    DialogContent,
    DialogTitle,
} from "@mui/material"
import ItemSelect from '../components/ItemSelect';


export default function CreateReportDialog({isOpen, onClose, onCreate}) {
    return (
        <Dialog
            open={isOpen}
            keepMounted
            onClose={onClose}
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
            <Button onClick={onCreate}>Создать</Button>
            <Button onClick={onClose}>Отменить</Button>
            </DialogActions>
        </Dialog>
    );
}