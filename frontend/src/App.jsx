import { Routes, Route } from "react-router-dom";
import HomePage from "@/components/HomePage"; // Assuming you have this too
import Navbar from "@/components/Navbar"
import "./index.css"

function App() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <Navbar />
            <Routes>
        <Route path="/" element={<HomePage />} />
      </Routes>
    </div>
  )
}

export default App
