//import Image from 'next/image'
import Header from "@/components/Header"
import SearchBox from "@/components/SearchBox"
import MusicBar from "@/components/MusicBar"
import styles from './styles/components/home.module.scss'

export default function Home() {
  return (
    <div className={`min-h-screen`}>
     <Header />
     <main className="flex min-h-screen flex-col mt-5 px-24">
      <SearchBox />
          <div className="songCover"></div>
          <div className="playlist"></div>
          <div className="mt-10">
        <div className={`${styles.musicBar} w-full`}>
            <MusicBar />
          </div>
        </div>
    </main>
    </div>
  )
}
