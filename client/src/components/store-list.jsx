"use client"

import { useState } from "react"
import { Link } from "react-router-dom"
import { MapPin, ChevronRight } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"
import PropTypes from 'prop-types'

export function StoreList({ stores }) {
  const [hoveredStore, setHoveredStore] = useState(null)

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {stores.map((store) => (
        <Link to={`/stores/${store.id}/recipes`} key={store.id}>
          <Card
            className={`transition-all duration-300 cursor-pointer h-full ${
              hoveredStore === store.id
                ? "border-emerald-500 shadow-lg transform -translate-y-1"
                : "border-slate-200 shadow-sm"
            }`}
            onMouseEnter={() => setHoveredStore(store.id)}
            onMouseLeave={() => setHoveredStore(null)}
          >
            <CardContent className="p-6 flex items-center">
              <div className="w-16 h-16 relative mr-4 flex-shrink-0">
                <img 
                  src={store.logo_url || "/placeholder.svg"} 
                  alt={store.name} 
                  className="object-contain w-full h-full"
                />
              </div>
              <div className="flex-1">
                <h3 className="font-semibold text-lg text-slate-800">{store.name}</h3>
                <div className="flex items-center text-slate-500 text-sm mt-1">
                  <MapPin className="h-4 w-4 mr-1" />
                  <span>View Deals</span>
                </div>
              </div>
              <ChevronRight
                className={`h-5 w-5 transition-colors ${
                  hoveredStore === store.id ? "text-emerald-500" : "text-slate-400"
                }`}
              />
            </CardContent>
          </Card>
        </Link>
      ))}
    </div>
  )
}

StoreList.propTypes = {
  stores: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      logo_url: PropTypes.string
    })
  ).isRequired
}
