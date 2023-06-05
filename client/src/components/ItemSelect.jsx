import * as React from 'react';
import {Select, MenuItem, InputLabel, FormControl} from '@mui/material';


export default function ItemSelect({ title, id, defaultValue, items, ...formProps }) {
    return (
        <FormControl { ...formProps } >
            <InputLabel id={ `${id}-label` }>{ title }</InputLabel>
            <Select
                labelId={ `${id}-label` }
                label={ title }
                defaultValue={ defaultValue }
            >
                { items.map(item => <MenuItem key={ item.value } value={ item.value }>{ item.label }</MenuItem>) }
            </Select>
        </FormControl>
    );
}