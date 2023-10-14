import Volume from '../app/svgs/volume.svg'
import LeftSeek from '../app/svgs/leftSeek.svg'
import RightSeek from '../app/svgs/rightSeek.svg'
import Play from '../app/svgs/play.svg'
import styles from '../app/styles/components/music.module.scss'

const MusicBar = () => {
    return (
        <div className="relative z-10 w-full">
            <div className={`${styles.musicbar} flex w-100 bg-black border-t-2 border-slate-500 shadow-white/5 ring-1 ring-slate-700/10`}>
                <div className="flex items-center space-x-4 px-6 py-4">
                <div className='h-6 w-6 flex-none'>
                    <LeftSeek />
                    </div>
                    <div className='h-10 w-10 flex-none'>
                    <Play />
                    </div>
                    <div className='h-6 w-6 flex-none'>
                    <RightSeek />
                    </div>
                   </div>
                <div className="flex flex-auto items-center border-l border-slate-200/60 pl-6 pr-4 text-[0.8125rem] leading-5 text-slate-700">
                 <div className='text-white'>00:51</div>
                    <div className="ml-4 flex flex-auto rounded-full bg-slate-100">
                        <div className="h-2 w-1/3 flex-none rounded-l-full rounded-r-[1px] bg-violet-600"></div>
                        <div className="-my-[0.3125rem] ml-0.5 h-[1.125rem] w-1 rounded-full bg-violet-600">
                            </div></div>
                            <div className="text-white ml-4">55:43</div>
                            <div className="ml-6 h-6 w-6 flex-none">
                            <Volume />
                            </div>
                </div>
            </div>
        </div>
    )
}

export default MusicBar;