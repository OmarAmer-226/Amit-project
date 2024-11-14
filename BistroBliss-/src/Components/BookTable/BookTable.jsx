import React, { useState } from "react";
import "./style.scss";
import "./MiddleWare.css";
import axios from "axios";
import toast from "react-hot-toast";
const BookTable = () => {
  const [getValue, SetValue] = useState({
    date: "",
    time: "",
    username: "",
    phone: "",
    total: "",
    type: "",
  });
  const sendData = async (Values) => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/bookTable/", Values);
      if(response.data.status === "success"){
        toast.success(response.data.msg);
      }else{
        toast.error("This didn't work.")
      }
    }catch(error){
      toast.error("An error occurred while booking the table.")
    }
    
  };
  const handleChange = (e) => {
    const takeValue = { ...getValue };
    takeValue[e.target.name] = e.target.value;
    SetValue({ ...takeValue });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    const CheckNumber = /^01[0125][0-9]{8}$/;
    const CheckUserName = /^[A-Z][a-z]$/;
      if (CheckUserName.test(getValue.username)) {
        if (CheckNumber.test(getValue.phone)) {
          sendData(getValue);
        } else {
          toast("You Must Enter The Correct Phone Number");
        }
      } else {
        toast(
          "Username Must Contain Not More than 8 Characters ,Start With Characters and end with Numbers",
          {
            duration: 5000,
          }
        );
      }

  };
  return (
    <div>
      <div className="parent-booktable">
        <div className="container-booktable">
          <div className="card">
            <div className="text">
              <h3 className="h3">Book A Table</h3>
              <p className="p">
                We consider all the drivers of change gives you the components
                you need to change to create a truly happens.
              </p>
            </div>
          </div>
          <div className="card">
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d8503056.848182853!2d37.68948679995415!3d28.94871469212754!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14fd844104b258a9%3A0xfddcb14b194be8e7!2z2YLYt9in2Lkg2LrYstmR2Kk!5e0!3m2!1sar!2seg!4v1709569529556!5m2!1sar!2seg"></iframe>
          </div>
          <form onSubmit={handleSubmit}>
            <div className="container-form">
              {/* New Line */}
              <div className="box-input">
                <div className="content-input">
                  <label htmlFor="date">date</label>
                  <input
                    type="date"
                    id="date"
                    name="date"
                    onChange={handleChange}
                    placeholder="25/03/2024"
                  />
                </div>
                <div className="content-input">
                  <label htmlFor="time">Time</label>
                  <input
                    type="time"
                    id="time"
                    name="time"
                    onChange={handleChange}
                    placeholder="06:30 PM"
                  />
                </div>
              </div>
              {/* New Line */}
              <div className="box-input">
                <div className="content-input">
                  <label htmlFor="name">UserName</label>
                  <input
                    type="text"
                    id="name"
                    name="username"
                    onChange={handleChange}
                    placeholder="Enter your name"
                  />
                </div>
                <div className="content-input">
                  <label htmlFor="phone">Phone</label>
                  <input
                    type="number"
                    id="phone"
                    name="phone"
                    onChange={handleChange}
                    placeholder="x-xxx-xxx-xxxx"
                  />
                </div>
              </div>
              {/* New Line */}
              <div className="box-input">
                <div className="content-input">
                  <label htmlFor="total">Total</label>
                  <input
                    type="text"
                    name="total"
                    id="total"
                    onChange={handleChange}
                    placeholder="1 Person"
                  />
                </div>
              </div>
              {/* New Line */}
              <button type="submit">Book A Table</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default BookTable;
