import { PostalForm } from "@/components/PostalForm"
import hero from "@/assets/hero.jpg"

export default function HomePage() {
  return (
    <section className="min-h-[80vh] flex items-center bg-white">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
          
          <div className="relative h-[500px] order-2 md:order-1">
            <img
              src={hero}
              alt="Fresh groceries and recipes"
              className="object-cover rounded-2xl shadow-lg w-full h-full"
            />
            <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/20 to-transparent rounded-2xl" />
          </div>
  
          {/* Content */}
          <div className="order-1 md:order-2">
            <h1 className="text-4xl md:text-5xl font-bold mb-4 tracking-tight text-slate-800">
              Find Local Deals & <span className="text-emerald-500">Create Recipes</span>
            </h1>
            <p className="text-lg text-slate-600 mb-8 max-w-md">
              Search for grocery flyers in your area and discover recipes based on the best deals available.
            </p>
            <PostalForm />
          </div>
        </div>
      </div>
    </section>
  )
}
