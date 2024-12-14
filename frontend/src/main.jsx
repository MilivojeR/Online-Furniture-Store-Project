import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

// router
import {
	RouterProvider,
	createBrowserRouter,
} from 'react-router-dom';

// pages
import HomePage from './pages/HomePage.jsx'; 
import ProductsPage from './pages/ProductsPage.jsx';
import SingleProductPage from './pages/SingleProductPage.jsx';



const router = createBrowserRouter([
  {
    path: '/',
    elmenet: <App />,
    children: [
      {
        path: '/',
        element: <HomePage />
      },
      {
        path: '/products',
        element: <ProductsPage />
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
