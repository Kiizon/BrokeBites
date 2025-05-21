import { useState, useEffect } from "react"
import { useSearchParams } from "react-router-dom"
import { PostalForm } from "@/components/PostalForm"
import { StoreList } from "@/components/store-list"

export default function BrowseStores() {
  const [searchParams] = useSearchParams()
  const [stores, setStores] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const postalCode = searchParams.get("postalCode")

  useEffect(() => {
    if (postalCode) {
      setIsLoading(true)
      fetch(`/api/stores?postal_code=${postalCode}`)
        .then(res => res.json())
        .then(data => {
          setStores(data)
          setIsLoading(false)
        })
        .catch(err => {
          console.error('Failed to fetch stores:', err)
          setIsLoading(false)
        })
    }
  }, [postalCode])

  return (
    <div>
      <div className="bg-slate-900 text-white py-6">
        <div className="container mx-auto px-4">
          <h1 className="text-2xl font-bold mb-4">Find Stores Near You</h1>
          <PostalForm />
        </div>
      </div>

      <div className="container mx-auto px-4 py-8">
        {postalCode ? (
          <div className="mb-6">
            <h2 className="text-xl font-semibold text-slate-800">
              {isLoading ? "Loading stores..." : `${stores.length} stores found near ${postalCode}`}
            </h2>
            <p className="text-slate-600">Click on a store to see recipes based on their current flyers</p>
            
            {!isLoading && <StoreList stores={stores} />}
          </div>
        ) : (
          <p className="text-slate-600">Enter your postal code to find stores near you.</p>
        )}
      </div>
    </div>
  )
}


