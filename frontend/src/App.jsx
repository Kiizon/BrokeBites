import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import RecipesPage from './pages/RecipesPage';
import RecipeDetailPage from './pages/RecipeDetailPage';
import Navbar from "@/components/Navbar"
import "./index.css"

function App() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen">
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/recipes/:storeId" element={<RecipesPage />} />
        <Route path="/recipe/:recipeId" element={<RecipeDetailPage />} />
      </Routes>
    </div>
  );
}

export default App;
