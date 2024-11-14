import React, { useState , useEffect } from "react";
import Css from "./Login.module.css";
import { RiLockPasswordLine } from "react-icons/ri";
import { CgMail } from "react-icons/cg";
import axios from "axios";
import toast from "react-hot-toast";
import { Link, useNavigate } from "react-router-dom";
import { FaRegUserCircle } from "react-icons/fa";

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
      e.preventDefault();
      try {
          const response = await axios.post('http://127.0.0.1:8000/login/',{
              username,
              password
          });
         alert(response.data.message);
      } catch (error) {
          console.error(error);
          alert('Login failed!');
      }
    };
 
  
  return (
    <div className={Css.bar}>
      <div className={Css.parent}>
        <div className={Css.container}>
          <form onSubmit={handleSubmit}>
            <div className={Css.logo}>
              <Link>
                <FaRegUserCircle />
              </Link>
            </div>
            <div className={Css.logo}>
              <h3>User Login</h3>
            </div>
            <div className={Css.login}>
              <label htmlFor="email">
                <CgMail />
              </label>
              <input
                type="text"
                id="username"
                value={username}
                name="username"
                onChange={(e) =>setUsername(e.target.value)} required
                placeholder="User Name"
              />
            </div>
            <div className={Css.login}>
              <label htmlFor="password">
                <RiLockPasswordLine />
              </label>
              <input
                type="password"
                value={password}
                name="password"
                onChange={(e) => setPassword(e.target.value)} required
                id="password"
                placeholder="Password"
              />
            </div>
            <div className={Css.create}>
              <Link to="/register" onClick={()=>window.scrollTo(0,100)}>Create New Account?</Link>
            </div>
            <button type="submit">Sign in</button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
