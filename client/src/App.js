import * as React from 'react';
import {Routes, Route, Navigate} from'react-router-dom';
import SignupPage from './pages/SignupPage';
import LoginPage from './pages/LoginPage';
import ReportsPage from './pages/ReportsPage';
import ReportDetailedPage from './pages/ReportDetailedPage';


export default function App() {
    return (
        <Routes>
            <Route path="/signup" element={<SignupPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/reports" element={<ReportsPage />} />
            <Route path="/reports/:uuid" element={<ReportDetailedPage />} />
            <Route path="*" element={<Navigate to="/reports" replace={true} />} />
        </Routes>  
    );
}
