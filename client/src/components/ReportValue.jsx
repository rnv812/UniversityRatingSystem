import { useState } from 'react';
import { Box, Typography, Checkbox, TextField, Divider } from '@mui/material'; 
import { usePatchReportValueMutation } from '../features/reports/reportsApiSlice';
import styles from '../styles/ReportValue.module.css';


export default function ReportValue({ indicator, valueType, value, id }) {
    const [val, setValue] = useState(value);
    const [patchReportValue] = usePatchReportValueMutation();

    async function handleOnChange(newValue) {
        setValue(newValue);
        try {
            if (valueType === 'float') {
                newValue = parseFloat(newValue)
            } else if (valueType === 'int') {
                newValue = parseInt(newValue, 10);
            }

            await patchReportValue({ id, newValue: {value: newValue, type: valueType} }).unwrap();  // TODO: debounce
        } catch (error) {
            setValue(value);
        }
    }

    function getInputElement() {
        if (valueType === 'bool') {
            return <Checkbox checked={ val } onChange={ e => handleOnChange(e.target.checked) } />;
        } else if (valueType === 'int' || valueType === 'float') {
            return <TextField sx={{ maxWidth: "80px" }} type='number' value={ val } onChange={ e => handleOnChange(e.target.value) } />
        } else {
            return <TextField sx={{ minWidth: "300px" }} value={ val } onChange={ e => handleOnChange(e.target.value) } />
        }
    }
    
    return (
        <>
            <Box className={ styles.lineBox }>
                <Box className={ styles.indicatorName }>
                    <Typography>{ indicator.name }</Typography>
                </Box>
                { getInputElement() }
            </Box>
            <Divider />
        </>
    )
}
