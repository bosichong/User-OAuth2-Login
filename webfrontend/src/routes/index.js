import Home from '../comconents/Home'
import Login from '../comconents/Login'

const routes = [
    {
        path: '/',
        element: <Home />
    },
    {
        path: '/home',
        element: <Home />
    },
    {
        path: '/login',
        element: <Login />
    },
]

export default routes