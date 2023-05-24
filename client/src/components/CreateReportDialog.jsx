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
import styles from '../styles/CreateReport.module.css';


export default function CreateReportDialog({isOpen, onClose, onCreate, availableYears, availableEducators}) {
    return (
        <Dialog
            open={isOpen}
            keepMounted
            onClose={onClose}
        >
            <DialogTitle>{"Создание анкеты"}</DialogTitle>
            <DialogContent>
                <Box style={{display:"flex", flexDirection: "column"}}>
                    <Box className={styles['select-box']}>
                        <ItemSelect
                            id={'report-educator'}
                            title={"Преподаватель"}
                            items={availableEducators }
                            sx={{width: "100%"}}
                        />
                    </Box>
                    <Box className={styles['select-box']}>
                        <ItemSelect
                            id={'report-year'}
                            title={"Год анкеты"}
                            items={availableYears}
                            sx={{width: "100%"}}
                        />
                    </Box>
                </Box>
            </DialogContent>
            <DialogActions>
            <Button onClick={onCreate}>Создать</Button>
            <Button onClick={onClose}>Отменить</Button>
            </DialogActions>
        </Dialog>
    );
}