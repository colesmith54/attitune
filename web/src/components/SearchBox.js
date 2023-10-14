import styles from '../app/styles/components/searchBox.module.scss'

const SearchBox = (props) => {

    async function logMovies() {
        const response = await fetch("http://localhost.com:5000/api/analyze_sentiment",{
            method: "POST", // *GET, POST, PUT, DELETE, etc.
            mode: "cors", // no-cors, *cors, same-origin
            cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
            credentials: "same-origin", // include, *same-origin, omit
            headers: {
              "Content-Type": "application/json",
            }
        });
        const movies = await response.json();
        console.log(movies);
    }
      
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