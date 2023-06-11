import { useState } from 'react';
import { Box, Typography, Checkbox, TextField } from '@mui/material'; 
import { usePatchReportValueMutation } from '../features/reports/reportsApiSlice';


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
            return <TextField type='number' value={ val } onChange={ e => handleOnChange(e.target.value) } />
        } else {
            return <TextField value={ val } onChange={ e => handleOnChange(e.target.value) } />
        }
    }
    
    return (
        <Box>
            <Typography>{ indicator.name }</Typography>
            { getInputElement() }
        </Box>
    )
}
