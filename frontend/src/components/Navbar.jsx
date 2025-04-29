import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";

function Navbar() {
  return (
    <header className="flex items-center justify-between px-8 py-4 bg-emerald-950 border-b text-white">
      <Button variant="ghost" asChild>
        <Link to="/" className="text-2xl font-bold">
          BrokeBites
        </Link>
      </Button>

      <nav className="flex items-center space-x-6">
        <Button variant="link" asChild>
          <Link to="/" className="hover:text-white text-white/70">
            Home
          </Link>
        </Button>
        <Button variant="link" asChild>
          <Link to="/deals" className="hover:text-white text-white/70">
            Deals
          </Link>
        </Button>
        <Button variant="link" asChild>
          <Link to="/recipes" className="hover:text-white text-white/70">
            Recipes
          </Link>
        </Button>
      </nav>
    </header>
  );
}

export default Navbar;
