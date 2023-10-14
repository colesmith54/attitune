//import Image from 'next/image'
import Header from "@/components/Header"
import SearchBox from "@/components/SearchBox"

export default function Home() {
  return (
    <>
     <Header />
     <main className="flex min-h-screen flex-col justify-between mt-5 px-24">
     
      <SearchBox />
    </main>
    </>
  )
}
