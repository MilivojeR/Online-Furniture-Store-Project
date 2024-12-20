import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import "bootstrap/dist/css/bootstrap.min.css";

// router
import {
	RouterProvider,
	createBrowserRouter,
} from 'react-router-dom';

// pages
import HomePage from './pages/HomePage.jsx'; 
import ProductsPage from './pages/ProductsPage.jsx';
import SingleProductPage from './pages/SingleProductPage.jsx';
import LoginPage from './pages/LoginPage.jsx';
import Header from './components/Header.jsx';



const router = createBrowserRouter([
  {
    path: '/',
    elmenet: <App />,
    children: [
      {
        path: '/',
        element: <><Header/><HomePage /></>
      },
      {
        path: '/products',
        element: <><Header/><ProductsPage /></>
      },
      {
        path: '/logIn',
        element: <LoginPage />
      },
      {
        path: '/singleProduct',
        element: <SingleProductPage />
      }
    ]
  }
])


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
