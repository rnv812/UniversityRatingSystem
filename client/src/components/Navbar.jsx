import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';


export default function Navbar({actions, fullname}) {
    return (
        <AppBar>
            <Toolbar>
                <Typography variant="h6" sx={{ flexGrow: 1 }}>
                    {fullname}
                </Typography>
                {actions.map(action => <Button color="inherit" key={action.name} onClick={action.func}>{action.name}</Button>)}
            </Toolbar>
        </AppBar>
  );
}