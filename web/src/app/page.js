//import Image from 'next/image'
import Header from "@/components/Header"
import SearchBox from "@/components/SearchBox"
import MusicBar from "@/components/MusicBar"
import styles from './styles/components/home.module.scss'
import Playlist from "@/components/Playlist"
import Iframe from 'react-iframe'

export default function Home() {
  return (
    <div className={`min-h-screen`}>
     <Header />
     <main className="flex min-h-screen flex-col mt-5 px-24">
      <SearchBox />
          <div className="col-md-6">
            <div className="playlist"><Playlist/></div>
          </div>
          <div className="songCover">
          <Iframe url="https://open.spotify.com/embed/track/2RlgNHKcydI9sayD2Df2xp?utm_source=generator"
                  width="640px"
                  height="320px"
                  id=""
                  className=""
                  display="block"
                  position="relative"/>
          </div>
          <div className="mt-10">
          <div className={`${styles.musicBar} w-full`}>
          </div>
        </div>
    </main>
    </div>
  )
}
