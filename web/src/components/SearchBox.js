'use client';
import styles from '../app/styles/components/searchBox.module.scss';

const SearchBox = (props) => {

    return (
        <div>
            <form method="post" onSubmit={props.handleFormSubmit}>
                <label htmlFor="search" className="block text-large font-large leading-6 text-white">How is your mood?</label>
                <div className="mt-2">
                    <textarea
                        id="search"
                        name="search_query"
                        rows="2"
                        className={`${styles.searchBox} border-white focus:border-[#7c3aed] rounded`}
                        value={props.searchQuery}
                        onChange={(e) => props.setSearchQuery(e.target.value)}
                    ></textarea>
                </div>
                <button type="submit" className="bg-violet-500 hover:bg-indigo-400 text-white font-semibold px-6 py-3 rounded-md">
                    Show Recommendations
                </button>
            </form>
        </div>
    )
};

export default SearchBox;
