import React, { useEffect, useState } from "react";
import Css from "./Dessart.module.css";
import axios from "axios";
import toast from "react-hot-toast";
const Dessert = () => {
const [Dessert, setProduct] = useState([]);
  useEffect(() => {
    async function getProduct() {
      try{
      const response = await fetch('http://127.0.0.1:8000/Dessert/')
      if(!response.ok){
        throw new Error ('Network response was not ok')
      }
       setProduct(await response.json())
       } catch (error) {
        console.error("Failed to fetch products:", error);
        toast.error("Failed to load products.");
       }
  }
  getProduct()

  }, []);
  return (
    <div>
      <div className={Css.parent}>
        <div className={Css.container}>
          {Dessert?.map((r,i) => (
            <div className={Css.card} key={i} data-aos="fade-zoom-in"
            data-aos-easing="ease-in-back"
            data-aos-delay="10"
            data-aos-offset="0">
              <div className={Css.img}>
                <img src={r.image} alt="" />
              </div>
              <div className={Css.text}>
                <h3>
                  <span>{r.price}</span>
                </h3>
                <h3 className={Css.h3}>{r.name}</h3>
                <p>{r.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
export default Dessert;
