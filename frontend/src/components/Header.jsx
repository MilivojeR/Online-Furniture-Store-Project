import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function Header() {
  const navigate = useNavigate();
  var token = sessionStorage.getItem("access_token");

  function login() {
    navigate("/logIn");
  }

  function logout() {
    token = null;
    sessionStorage.clear();
    toast.success("Successfully logout");
    setTimeout(() => {
      navigate("/");
    }, 500);
  }

  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-dark bg-warning">
        <a className="navbar-brand ms-4" href="/">
          DeskESSENTIALS
        </a>
        <div className="container-fluid">
          <ul className="navbar-nav d-flex w-100">
            <li className="nav-item active">
              <Link className="nav-link" to="/">
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/products">
                Products
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/">
                About us
              </Link>
            </li>
            {token == null ? (
              <li className="nav-item ms-auto">
                <button className="btn btn-danger" onClick={() => login()}>
                  Log in
                </button>
              </li>
            ) : (
              <li className="nav-item ms-auto">
                <button className="btn btn-danger" onClick={() => logout()}>
                  Log out
                </button>
              </li>
            )}
          </ul>
        </div>
      </nav>
    </div>
  );
}

export default Header;
