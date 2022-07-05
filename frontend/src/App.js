import { Header } from "./components/Header";
import { Footer } from "./components/Footer";
import { Contact } from "./components/Contact";
import { Middle } from "./components/Middle";
import {Download} from "./components/Download";
import "./App.css";
import {
  BrowserRouter as Router,
  Routes, // Just Use Routes instead of "Switch"
  Route
} from "react-router-dom";

function App() {
  return (
    <>
      <Router>
        <Header />
        <Routes>
          
        <Route exact path="/download/:unique" element={<Download />} />
        <Route exact path="/" element={<Middle />} />
          <Route exact path="/contact" element={<Contact />} />
          
        </Routes>
        <Footer />
        
      </Router>
    </>
  );
}

export default App;
