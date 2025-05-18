import { NavLink } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ShoppingBasket } from "lucide-react";

{/* define navigation links*/}
const navLinks = [
  { to:"/", label: "Home"},
  { to:"/browse-stores", label: "Browse Stores"},
  { to: "/saved-recipes", label: "My Recipes"},
];

export default function Navbar() {
  return (
    <header className="fixed top-0 left-0 right-0 border-b border-slate-200 bg-white z-50">
      <div className="container mx-auto px-4 py-3 flex items-center justify-between"> 
        
        {/* logo */}
        <NavLink to="/" className="flex items-center gap-2" aria-label="BrokeBites Home">
          <ShoppingBasket className="h-6 w-6 text-emerald-500" aria-hidden="true" />
          <span className="font-bold text-xl text-slate-800">BrokeBites</span>
        </NavLink>

        {/* highlight active  */}
        <nav aria-label="Primary Nagivation" className="flex items-center gap-6">
          {navLinks.map(({to, label}) => (
            <NavLink
              key={to}
              to={to}
              className={({isActive}) =>
                isActive
                ? "text-emerald-500 font-medium focus-visible:ring-2 focus-visible:ring-emerald-500"
                : "text-slate-600 hover:text-slate-900 focus-visible:ring-2 focus-visible:ring-emerald-500"
            }
            >
              {label}
            </NavLink>
          ))}
        </nav>
        
        {/* sign-in/sign-up*/}
        <div className="flex items-center gap-2">
          <Button asChild variant="ghost" >
            <NavLink to="/sign-in"> Sign In </NavLink>
          </Button>
          <Button asChild className="bg-emerald-500 hover:bg-emerald-600">
            <NavLink to="/sign-up" > Sign Up </NavLink>
            </Button>
        </div>
      </div>
    </header>
  )
}