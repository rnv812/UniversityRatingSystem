import { useLocation, Navigate, Outlet } from "react-router-dom"
import { useSelector } from "react-redux"
import { selectIsAuthenticated } from "./authSlice"

const RequireAuth = () => {
    const isAuthenticated = useSelector(selectIsAuthenticated)
    const location = useLocation()

    return (
        isAuthenticated
            ? <Outlet />
            : <Navigate to="/login" state={{ from: location }} replace />
    )
}
export default RequireAuth