import { useState } from "react";
import { Button, TextField, Box, Dialog, DialogActions, DialogContent, DialogTitle } from "@mui/material"
import styles from '../styles/CreateReport.module.css';
import { useGetEducatorMeQuery } from "../features/educators/educatorsApiSlice";
import { useCreateReportMutation } from "../features/reports/reportsApiSlice";


export default function CreateReportDialog({ isOpen, onClose }) {
    const [year, setYear] = useState(new Date().getFullYear());
    const { data: educator, isLoading: educatorLoading } = useGetEducatorMeQuery();
    const [createReport] = useCreateReportMutation();

    async function onCreateReport() {
        if (educatorLoading) {
            return;
        }

        try {
            await createReport({year, educatorId: educator.id });
        } catch (error) {
            alert(error.message); // TODO: non devil way for error notification 
        }

        onClose();
    }

    return (
        <Dialog
            open={ isOpen }
            keepMounted
            onClose={ onClose }
        >
            <DialogTitle>{"Укажите отчётный год"}</DialogTitle>
            <DialogContent>
                <Box className={ styles.fieldsContainer }>
                    <Box className={ styles.selectBox }>
                        <TextField sx={{ width: "100%" }} type='number' value={ year } onChange={ e => {setYear(e.target.value)} } />
                    </Box>
                </Box>
            </DialogContent>
            <DialogActions>
            <Button onClick={ onCreateReport }>Создать</Button>
            <Button onClick={ onClose }>Отменить</Button>
            </DialogActions>
        </Dialog>
    );
}