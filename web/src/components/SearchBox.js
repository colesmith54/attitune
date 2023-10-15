'use client';
import styles from '../app/styles/components/searchBox.module.scss';

const SearchBox = (props) => {
    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            props.handleFormSubmit(e);
        }
    };
    return (
        <div className='my-4 md:my-10 mx-4 md:mx-0'>
            <form method="post" onSubmit={props.handleFormSubmit}>
                <label htmlFor="search" className="block text-large font-large leading-6 text-white">How is your mood?</label>
                <div className="mt-2">
                <textarea
                    id="search"
                    name="search_query"
                    placeholder="Enter your mood... get matching songs..."
                    rows="2"
                    className={`${styles.searchBox} border-white focus:border-[#7c3aed] rounded`}
                    value={props.searchQuery}
                    onChange={(e) => props.setSearchQuery(e.target.value)}
                    onKeyDown={handleKeyDown}
                ></textarea>
                </div>
                <div className='text-center md:text-left'>
                <button type="submit" className="w-full md:max-w-xs bg-violet-500 hover:bg-indigo-400 text-white font-semibold my-2 md:my-8 px-6 py-3 rounded-md">
                    Show Recommendations
                </button>
                </div>
            </form>
        </div>
    )
};

export default SearchBox;
