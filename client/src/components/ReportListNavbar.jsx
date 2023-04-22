import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

export default function ReportListNavbar() {
    return (
        <AppBar>
            <Toolbar>
                <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                    Фамилия Имя Отчество
                </Typography>
                <Button color="inherit">Создать анкету</Button>
                <Button color="inherit">Выйти</Button>
            </Toolbar>
        </AppBar>
  );
}