import { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useNavigate } from 'react-router-dom';

export default function HomePage() {
  const [postalCode, setPostalCode] = useState('');
  const [stores, setStores] = useState([]);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handlePostalCodeSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch('http://localhost:5000/api/flyers', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ postal_code: postalCode }),
      });
      const data = await response.json();
      setStores(data);
    } catch (error) {
      console.error('Error fetching stores:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleStoreSelect = async (storeId) => {
    try {
      const response = await fetch(`http://localhost:5000/api/flyers/${storeId}/recipes`);
      const recipes = await response.json();
      console.log('Received recipes:', recipes);
      if (recipes.error) {
        console.error('Error from server:', recipes.error);
        return;
      }
      navigate(`/recipes/${storeId}`, { state: { recipes } });
    } catch (error) {
      console.error('Error fetching recipes:', error);
    }
  };

  return (
    <div className="container mx-auto p-4">
      <Card className="max-w-md mx-auto">
        <CardHeader>
          <CardTitle>Find Recipes Based on Local Deals</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handlePostalCodeSubmit} className="space-y-4">
            <div>
        <Input
          type="text"
                placeholder="Enter your postal code"
          value={postalCode}
                onChange={(e) => setPostalCode(e.target.value)}
                required
        />
            </div>
            <Button type="submit" disabled={loading}>
              {loading ? 'Loading...' : 'Find Stores'}
            </Button>
          </form>

          {stores.length > 0 && (
            <div className="mt-6">
              <h2 className="text-xl font-semibold mb-4">Available Stores</h2>
              <div className="space-y-2">
                {stores.map((store) => (
                  <Button
                    key={store.id}
                    variant="outline"
                    className="w-full"
                    onClick={() => handleStoreSelect(store.id)}
                  >
                    {store.merchant}
                  </Button>
                ))}
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
