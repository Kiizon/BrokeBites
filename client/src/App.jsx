import { Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import RecipesPage from './pages/RecipesPage';
import RecipeDetailPage from './pages/RecipeDetailPage';
import Navbar from "@/components/Navbar"
import { SignInForm } from "@/components/auth/SignInForm"
import { SignUpForm } from "@/components/auth/SignUpForm"
import  BrowseStores from "@/pages/BrowseStores"
import SavedRecipes from "@/pages/SavedRecipes"
import "./index.css"

function App() {
  return (
    <div className="min-h-screen">
      <Navbar />
      <main className="pt-16">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/recipes/:storeId" element={<RecipesPage />} />
          <Route path="/recipe/:recipeId" element={<RecipeDetailPage />} />
          <Route path="/browse-stores" element={<BrowseStores/>} />
          <Route path="/saved-recipes" element={<SavedRecipes/>} />
          <Route path="/sign-up" element={<SignUpForm />} />
          <Route path="/sign-in" element={<SignInForm/>} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
