import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { Search } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export function PostalForm() {
  const [postalCode, setPostalCode] = useState("")
  const [isLoading, setIsLoading] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setIsLoading(true)

    try {
      const res = await fetch(`/api/stores?postal_code=${postalCode}`)
      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`)
      }
      const stores = await res.json()
      
      if (stores.length > 0) {
        navigate(`/browse-stores?postalCode=${encodeURIComponent(postalCode)}`)
      } else {
        // Handle no stores found
        console.log('No stores found')
      }
    } catch (err) {
      console.error('Failed to fetch stores:', err)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <form onSubmit={handleSubmit} className="flex w-full max-w-md">
      <div className="relative flex-1">
        <Input
          type="text"
          placeholder="Enter your postal code"
          className="pr-10 h-12 border-slate-300 focus:border-emerald-500 focus:ring-emerald-500 text-slate-800 placeholder:text-slate-400 rounded-l-md"
          value={postalCode}
          onChange={(e) => setPostalCode(e.target.value)}
          required
        />
        <Search className="absolute right-3 top-1/2 -translate-y-1/2 h-5 w-5 text-slate-400" />
      </div>
      <Button
        type="submit"
        className="ml-0 h-12 px-6 bg-emerald-500 hover:bg-emerald-600 rounded-l-none"
        disabled={isLoading}
      >
        {isLoading ? "Searching..." : "Search"}
      </Button>
    </form>
  )
}
