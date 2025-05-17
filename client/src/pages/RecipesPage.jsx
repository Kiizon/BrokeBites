import { useLocation, useNavigate } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function RecipesPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const { recipes = [] } = location.state || {};

  const handleRecipeClick = (recipe) => {
    navigate(`/recipe/${recipe.id}`, { state: { recipe } });
  };

  // Ensure recipes is an array and has the required properties
  const validRecipes = Array.isArray(recipes) ? recipes : [];

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-6">Recipes Based on Available Deals</h1>
      {validRecipes.length === 0 ? (
        <p className="text-center text-gray-600">No recipes available at the moment.</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {validRecipes.map((recipe) => (
            <Card key={recipe.id || Math.random()} className="cursor-pointer hover:shadow-lg transition-shadow">
              <CardHeader>
                <CardTitle>{recipe.title || 'Untitled Recipe'}</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-gray-600 mb-4">{recipe.description || 'No description available.'}</p>
                <Button onClick={() => handleRecipeClick(recipe)}>
                  View Recipe
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
} 