import * as React from 'react';
import {Box} from '@mui/material';
import {connect} from 'react-redux';
import { checkAuthenticated, loadUser } from '../actions/auth';


function Layout(props) {
    React.useEffect(() => {
        props.checkAuthenticated();
        props.loadUser();
    });

    return (
        <Box>
            {props.children}
        </Box>
    );
}

export default connect(null, { checkAuthenticated, loadUser })(Layout);