import * as React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';


export default function Navbar({ actions, pageTitle }) {
    return (
        <AppBar>
            <Toolbar>
                <Typography variant="h6" sx={{ flexGrow: 1 }}>
                    {pageTitle}
                </Typography>
                { actions.map(action => <Button color="inherit" key={ action.name } onClick={ action.func }>{ action.name }</Button>) }
            </Toolbar>
        </AppBar>
  );
}