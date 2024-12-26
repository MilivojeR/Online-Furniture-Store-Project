import React from "react";
import { Link, useNavigate } from "react-router-dom";
import greenChair from "../assets/greenChair.png";

function HomePage() {
  const navigate = useNavigate();

  function products() {
    navigate("/products");
  }
  return (
    <div className="bg-gradient-to-b from-amber-400 to-lime-950 flex flex-col items-center min-h-screen">
      <div className="flex items-center justify-between w-full">
        <div className="text-white flex-col justify-center ml-20">
          <p className="text-4xl">
            Organize with <br /> Style
          </p>
          <p>A new collection of desk chairs is available for purchase.</p>
          <button className="btn btn-danger" onClick={() => products()}>
            Shop Now
          </button>
        </div>
        <div>
          <img src={greenChair} alt="Green Chair" />
        </div>
      </div>
      <div className="w-full mt-30"></div>
    </div>
  );
}

export default HomePage;
