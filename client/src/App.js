import * as React from 'react';
import {Routes, Route} from'react-router-dom';
import LoginPage from './pages/LoginPage';
import ReportsPage from './pages/ReportsPage';
import NotFoundPage from './pages/NotFoundPage';


export default function App() {
    return (
        <Routes>
            <Route path="/login" element={<LoginPage />} />

            <Route path="/reports" element={<ReportsPage />} />
            <Route path="*" element={<NotFoundPage />} />
        </Routes>  
    );
}
