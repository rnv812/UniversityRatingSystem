import { Routes, Route } from 'react-router-dom'
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import ActivateAccountPage from './pages/ActivateAccountPage';
import ReportsPage from './pages/ReportsPage';
import ReportDetailsPage from './pages/ReportDetailsPage';
import RequireAuth from './features/auth/RequireAuth';
import Layout from './layouts/Layout';


export default function App() {
    return (
        <Routes>
            <Route path="/" element={<Layout />}>
                {/* public routes */}
                <Route path="/login" element={<LoginPage />} />
                <Route path="/signup" element={<SignupPage />} />
                <Route path="/activate/:uid/:token" element={<ActivateAccountPage />} />

                {/* protected routes */}
                <Route element={<RequireAuth />}>
                    <Route path="/reports" element={<ReportsPage />} />
                    <Route path="/reports/:uuid" element={<ReportDetailsPage />} />
                </Route>
            </Route>
        </Routes>
    );
}
