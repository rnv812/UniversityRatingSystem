import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

export default function Navbar({actions}) {
    return (
        <AppBar>
            <Toolbar>
                <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                    Фамилия Имя Отчество
                </Typography>
                {actions.map(action => <Button color="inherit" onClick={action.func}>{action.name}</Button>)}
            </Toolbar>
        </AppBar>
  );
}