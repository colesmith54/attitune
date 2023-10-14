//import Image from 'next/image'
import SearchBox from "@/components/SearchBox"

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col justify-between p-24">
      <SearchBox />
    </main>
  )
}
