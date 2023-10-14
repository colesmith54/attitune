import Header from "@/components/Header";
import SearchBox from "@/components/SearchBox";
import styles from './styles/components/home.module.scss';
import Playlist from "@/components/Playlist";
import IframePopup from "@/components/IframePopup";

export default function Home() {
  return (
    <div className={`min-h-screen`}>
      <Header />
      <main className="flex min-h-screen flex-col mt-5 px-24">
        <SearchBox />
        <div className="col-md-6">
          <div className="playlist"><Playlist/></div>
        </div>

        <IframePopup 
          url="https://open.spotify.com/embed/track/2RlgNHKcydI9sayD2Df2xp?utm_source=generator"
        />
      </main>
    </div>
  )
}
