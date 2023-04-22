import * as React from 'react';
import {Box, TextField} from '@mui/material';
import ItemSelect from './ItemSelect';
import styles from '../styles/ReportListFilter.module.css';


export default function ReportListFilter() {
    return (
        <Box className={styles.filterItems}>
            <ItemSelect
                id={'report-owner-filter-select'}
                title={"Показывать"}
                items={[{label: "Свои", value: "own"}, {label: "Все", value: "all"}]}
                defaultValue={"own"}
                sx={{ minWidth: 100 }}
            />

            <ItemSelect
                id={'report-status-filter-select'}
                title={"Статус"}
                items={[{label: "Не выбрано", value: ""}, {label: "Подтверждена", value: "approved"}, {label: "На рассмотрении", value: "pending"}]}
                defaultValue={""}
                sx={{ minWidth: 190 }}
            />

            <TextField label="Год" variant="outlined" type='number' sx={{ minWidth: 120 }} />
            
            <TextField label="ФИО Преподавателя" variant="outlined" sx={{ minWidth: 300 }} />

            <ItemSelect
                id={'report-sort-method-select'}
                title={"Сортировка"}
                items={[{label: "ФИО", value: "year"}, {label: "Год", value: "name"}]}
                defaultValue={"year"}
                sx={{ minWidth: 120 }}
            />
        </Box>
    );
}
