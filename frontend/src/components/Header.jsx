import React from 'react';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <div>
        <nav className='navbar navbar-expand-lg navbar-dark bg-warning'>
            <a className='navbar-brand ms-4' href='/'>Online furniture store</a>
            <div className='container-fluid'>
                <ul className='navbar-nav d-flex w-100'>
                    <li className='nav-item active'>
                        <Link className='nav-link' to='/'>Home</Link>
                    </li>
                    <li className='nav-item'>
                        <Link className='nav-link' to='/products'>Products</Link>
                    </li>
                    <li className='nav-item'>
                        <Link className='nav-link' to='/'>About us</Link>
                    </li>
                    <li className='nav-item ms-auto'>
                        <button className='btn btn-danger'>Log in</button>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
  )
}

export default Header