import React, { useState } from "react";
import Css from "./Register.module.css";
import { CgMail } from "react-icons/cg";
import { RiLockPasswordLine } from "react-icons/ri";
import { FaRegUser, FaRegUserCircle } from "react-icons/fa";
import axios from "axios";
import { Link} from "react-router-dom";
const Register = () => {

  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
      e.preventDefault();
      try {
          const response = await axios.post('http://127.0.0.1:8000/register/', {
              username,
              email,
              password
          });
          alert('Registration successful!');
      } catch (error) {
          console.error(error);
          alert('Registration failed!');
      }}

  return (
    <div>
      <div className={Css.parent}>
        <form onSubmit={handleSubmit}>
          <div className={Css.logo}>
            <Link>
              <FaRegUserCircle />
            </Link>
          </div>
          <div className={Css.logo}>
            <h3>Create Account</h3>
          </div>
          <div className={Css.login}>
            <label htmlFor="username">
              <FaRegUser />
            </label>
            <input
              type="text"
              id="username"
              name="username"
              value={username}
              onChange={(e)=> setUsername(e.target.value)}required
              placeholder="UserName"
            />
          </div>
          <div className={Css.login}>
            <label htmlFor="email">
              <CgMail />
            </label>
            <input
              type="email"
              id="email"
              name="email"
              value={email}
              onChange={(e)=> setEmail(e.target.value)}required
              placeholder="Address your email"
            />
          </div>
          <div className={Css.login}>
            <label htmlFor="password">
              <RiLockPasswordLine />
            </label>
            <input
              type="password"
              name="password"
              value={password}
              onChange={(e)=> setPassword(e.target.value)}required
              id="password"
              placeholder="Password"
            />
          </div>
          <div className={Css.create}>
            <Link to="/login">Already have an account?</Link>
          </div>
          <button type="submit"> Create</button>
        </form>
      </div>
    </div>
  );
};

export default Register;
