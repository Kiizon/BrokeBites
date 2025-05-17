import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ShoppingBasket } from "lucide-react";

export default function Navbar() {
  return (
    <header className="fixed top-0 left-0 right-0 border-b border-slate-200 bg-white z-50">
      <div className="container mx-auto px-4 py-3 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-2">
          <ShoppingBasket className="h-6 w-6 text-emerald-500" />
          <span className="font-bold text-xl text-slate-800">FlyerRecipes</span>
        </Link>

        <nav className="hidden md:flex items-center gap-6">
          <Link to="/" className="text-slate-600 hover:text-slate-900">
            Home
          </Link>
          <Link to="/stores" className="text-slate-600 hover:text-slate-900">
            Browse Stores
          </Link>
          <Link to="#" className="text-slate-600 hover:text-slate-900">
            How It Works
          </Link>
        </nav>

        <div className="flex items-center gap-2">
          <Button variant="ghost" className="text-slate-600">
            Sign In
          </Button>
          <Button className="bg-emerald-500 hover:bg-emerald-600">Sign Up</Button>
        </div>
      </div>
    </header>
  )
}