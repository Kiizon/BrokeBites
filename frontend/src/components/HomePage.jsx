import { useState } from 'react';
import { Input } from "@/components/ui/input";

function HomePage() {
  const [postalCode, setPostalCode] = useState('');

  const handleInputChange = (event) => {
    setPostalCode(event.target.value);
  };
  
  const handleFindDeals = (event) => {
    event.preventDefault(); // prevent page reload
    console.log(`Finding deals for postal code: ${postalCode}`);
  }

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4">
      <h1 className="text-2xl font-bold mb-4">Enter your postal code to find flyers near you</h1>

      <form onSubmit={handleFindDeals} className="flex flex-col gap-4 w-full max-w-sm">
        <Input
          type="text"
          placeholder="Postal Code"
          value={postalCode}
          onChange={handleInputChange}
        />
        <button
          type="submit"
          className="bg-black text-white py-2 px-4 rounded hover:bg-gray-800"
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default HomePage;
