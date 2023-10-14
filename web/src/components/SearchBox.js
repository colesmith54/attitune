'use client';
import { useState, useEffect } from 'react';
import styles from '../app/styles/components/searchBox.module.scss';

const SearchBox = (props) => {
    const [searchQuery, setSearchQuery] = useState('');
    const [loadedFromStorage, setLoadedFromStorage] = useState(false);

    const handleSubmit = (data) => {
        const formData = new FormData();
        formData.append('search_query', data);
        
        fetch("http://127.0.0.1:5000/api/analyze_sentiment", {
            method: 'post',
            mode: "cors",
            cache: "no-store",
            credentials: "same-origin",
            body: formData
        });

        localStorage.setItem('search_query', data); // Use localStorage instead
    };

    useEffect(() => {
        const storedQuery = localStorage.getItem('search_query'); // Use localStorage instead
        if (storedQuery) {
            setSearchQuery(storedQuery);
            setLoadedFromStorage(true);
        }
    }, []);

    useEffect(() => {
        if (loadedFromStorage) {
            handleSubmit(searchQuery);
            setLoadedFromStorage(false); 
        }
    }, [loadedFromStorage]);

    useEffect(() => {
        const handleBeforeUnload = (e) => {
            const windowsCount = window.open(null, '_self').length;
            if (windowsCount === 1) { // If only one window/tab is open
                localStorage.removeItem('search_query'); // Clear the stored data
            }
        };

        window.addEventListener('beforeunload', handleBeforeUnload);

        return () => {
            window.removeEventListener('beforeunload', handleBeforeUnload);
        };
    }, []);

    const handleFormSubmit = (e) => {
        e.preventDefault();
        handleSubmit(searchQuery);  
    };

    return (
        <div>
            <form method="post" onSubmit={handleFormSubmit}>
                <label htmlFor="search" className="block text-large font-large leading-6 text-white">How is your mood?</label>
                <div className="mt-2">
                    <textarea
                        id="search"
                        name="search_query"
                        rows="2"
                        className={`${styles.searchBox} border-white focus:border-[#7c3aed] rounded`}
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
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
