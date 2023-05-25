import * as React from 'react';
import {Routes, Route, Navigate} from'react-router-dom';
import SignupPage from './pages/SignupPage';
import ActivateAccountPage from './pages/ActivateAccountPage';
import LoginPage from './pages/LoginPage';
import ReportsPage from './pages/ReportsPage';
import ReportDetailedPage from './pages/ReportDetailedPage';
import { Provider } from 'react-redux';
import store from './store';


export default function App() {
    return (
        <Provider store={store}>
            <Routes>
                <Route path="/signup" element={<SignupPage />} />
                <Route path="/activate/:uid/:token" element={<ActivateAccountPage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/reports" element={<ReportsPage />} />
                <Route path="/reports/:uuid" element={<ReportDetailedPage />} />
                <Route path="*" element={<Navigate to="/login" replace={true} />} />
            </Routes>
        </Provider>
          
    );
}

