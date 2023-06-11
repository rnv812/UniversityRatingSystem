import React from 'react'
import { Box } from '@mui/material';
import { useGetIndicatorsQuery } from '../features/rating/ratingApiSlice';
import ReportValue from './ReportValue';


export default function ReportForm({ reportValues }) {
    const { data, isLoading } = useGetIndicatorsQuery();
    const indicatorsMap = isLoading ? new Map() : buildIndicatorsMap();

    function buildIndicatorsMap() {
        let indicatorsMap = new Map();
        for (let indicator of data) {
            indicatorsMap.set(indicator.id, indicator)
        }
        return indicatorsMap;
    }

    return (
        <Box>
            { isLoading || !reportValues
                ? "Загрузка..." 
                : reportValues.map(
                    item => <ReportValue
                        key={ item.id }
                        id={ item.id }
                        valueType={ item.value.type }
                        value={ item.value.value }
                        indicator={ indicatorsMap.get(item.indicator) }
                    />
            ) }
        </Box>
    )
}
