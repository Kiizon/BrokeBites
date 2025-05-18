import { ShoppingBasket } from "lucide-react"

export function Footer() {
  return (
    <footer className="bg-white border-t border-slate-200 py-6">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between items-center">
          <div className="flex items-center gap-2 mb-4 md:mb-0">
            <ShoppingBasket className="h-5 w-5 text-emerald-500" />
            <span className="font-semibold text-slate-800"></span>
          </div>


          <div className="text-sm text-slate-500">© {new Date().getFullYear()} Kish Dizon</div>
        </div>
      </div>
    </footer>
  )
}
