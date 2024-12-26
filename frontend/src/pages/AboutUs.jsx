import React from "react";

function AboutUs() {
  return (
    <div className="bg-gradient-to-b from-amber-400 to-lime-950 flex flex-col items-center min-h-screen">
      <div className="text-white flex-col justify-center ml-20">
        <h1 class="mt-10">About Us</h1>
        <p>
          Welcome to DeskESSENTIALS, your one-stop shop for all your office
          supply needs. We are dedicated to providing you with the best products
          to enhance your workspace, whether you're working from home or in a
          corporate office.
        </p>
        <h1>Our Mission</h1>
        <p>
          At DeskESSENTIALS, our mission is to make your work environment more
          efficient, organized, and stylish. We believe that a well-equipped
          workspace can boost productivity and creativity, and we are here to
          help you achieve that.
        </p>
        <h1>Our Products </h1>
        <p>
          We offer a wide range of office supplies, including:
          <ul class="ps-5 mt-2 space-y-1 list-disc list-inside">
            <li>Ergonomic desk chairs</li>
            <li>High-quality stationery</li>
            <li>Innovative storage solutions</li>
            <li>Stylish desk accessories</li>
          </ul>
          And much more!
        </p>
        <h1>Our story</h1>
        <p>
          DeskESSENTIALS was founded with the vision of transforming ordinary
          workspaces into extraordinary ones. Our team is passionate about
          office supplies and understands the importance of a well-organized and
          inspiring workspace. We are constantly on the lookout for the latest
          trends and innovations to bring you the best products on the market.
          Thank you for choosing DeskESSENTIALS. We look forward to helping you
          create a workspace that you love.
        </p>
      </div>
    </div>
  );
}
export default AboutUs;
