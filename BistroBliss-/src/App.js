import { Route, Routes } from "react-router-dom";
import Home from "./Components/Home/Home/Home";
import About from "./Components/About/About/About";
import Menu from "./Components/menu/Menu/Menu";
import BreakFast from "./Components/menu/BreakFast/BreakFast";
import AllProducts from "./Components/menu/AllProducts/allProducts";
import Dishes from "./Components/menu/Dishes/Dishes";
import Drinks from "./Components/menu/Drinks/Drinks";
import Dessert from "./Components/menu/Dessert/Dessart";
import Pages from "./Components/Pages/Pages/Pages";
import Contact from "./Components/Contact/Contact/Contact";
import NoPage from "./Components/NoPage/NoPage";
import Login from "./Components/Register&Login/Login/Login";
import Register from "./Components/Register&Login/Register/Register";
import NavBar from "./Components/NavBar/NavBar";
import Footer from "./Components/Footer/Footer";
import { Toaster } from "react-hot-toast";
import BookTable from "./Components/BookTable/BookTable";
import Aos from "aos";
import "aos/dist/aos.css";
import { useEffect } from "react";

function App() {
  useEffect((r) => {
    Aos.init({ duration: 2000 });
  }, []);
  return (
    <div className="App">
      <Toaster position="top-center" reverseOrder={true} />
      <NavBar />
      <Routes>
        {/* Here for all Compnent in NavBary */}
        <>
          <Route index element={<Home />} />
          <Route path="about" element={<About />} />
        </>
        {/* Here for End all Compnent in NavBary */}

        {/* Here for OutLet to Menu */}
        <>
          <Route
            path="/menu"
            element={<Menu />}
            children={<Route path="/menu" element={<AllProducts />} />}
          />
          <Route
            path="menu"
            element={<Menu />}
            children={<Route path="/menu/breakfast" element={<BreakFast />} />}
          />
          <Route
            path="menu"
            element={<Menu />}
            children={<Route path="/menu/dishes" element={<Dishes />} />}
          />
          <Route
            path="menu"
            element={<Menu />}
            children={<Route path="/menu/drink" element={<Drinks />} />}
          />
          <Route
            path="menu"
            element={<Menu />}
            children={<Route path="/menu/dessert" element={<Dessert />} />}
          />
        </>
        {/* Here End for OutLet to Menu */}
        
        {/* Here For End DashBord */}
        {/* Here for all Compnent in NavBary */}
        <>
          <Route path="pages" element={<Pages />} />
          <Route path="contact" element={<Contact />} />
          <Route path="*" element={<NoPage />} />
          <Route path="/register" element={<Register />} />
          <Route path="/booktable" element={<BookTable />} />
          <Route path="/login" element={<Login />} />
        </>
        {/* Here for End all Compnent in NavBar */}
      </Routes>
      {/* <Loading/> */}
      <Footer />
    </div>
  );
}
export default App;

