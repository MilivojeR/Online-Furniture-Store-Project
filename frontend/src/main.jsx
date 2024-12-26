import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import "bootstrap/dist/css/bootstrap.min.css";
import {toast, ToastContainer} from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

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
        element: <><Header/><ToastContainer position="top-center" autoClose={1000} /><HomePage /></>
      },
      {
        path: '/products',
        element: <><Header/><ToastContainer position="top-center" autoClose={1000} /><ProductsPage /></>
      },
      {
        path: '/logIn',
        element: <><Header/><ToastContainer position="top-center" autoClose={1000} /><LoginPage /></>
      },
      {
        path: '/singleProduct/:id',
        element: <><Header/><ToastContainer position="top-center" autoClose={1000} /><SingleProductPage /></>
      }
    ]
  }
])


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
