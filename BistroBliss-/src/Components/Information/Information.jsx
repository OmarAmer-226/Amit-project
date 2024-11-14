import React from "react";
import Css from "./Information.module.css";
import { CiPhone, CiMail } from "react-icons/ci";
import { FaFacebookF, FaGithub, FaLinkedinIn } from "react-icons/fa";
import { Link } from "react-router-dom";
const Information = () => {
  return (
    <div>
      <div className={Css.parent}>
        <div className={Css.container}>
          <div className={Css.call}>
            <div className={Css.text}>
              <button>
                <CiPhone />
              </button>
              <p>+2011111111</p>
            </div>
            <div className={Css.text}>
              <button>
                <CiMail />
              </button>
              <p>o*****@gmail.com</p>
            </div>
          </div>
          <div className={Css.icons}>
            <Link to="#">
              <FaFacebookF />
            </Link>
            <Link to="#">
              <FaGithub />
            </Link>
            <Link to="#">
              <FaLinkedinIn  />
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Information;
