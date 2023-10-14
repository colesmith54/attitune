import styles from '../app/styles/components/searchBox.module.scss'

const SearchBox = (props) => {
    return(
        <div>
            <label htmlFor="search" className="block text-sm font-medium leading-6 text-white">How is your mood?</label>
            <div className="mt-2">
              <textarea id="search" name="search" rows="3" className={`${styles.searchBox} border-white focus:border-[#7c3aed] rounded`}></textarea>
            </div>
        </div>
    )
}

export default SearchBox