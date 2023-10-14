'use client';
import { useState } from 'react';
import styles from '../app/styles/components/searchBox.module.scss'

const SearchBox = (props) => {

    const handleSubmit = (e) => {
        e.preventDefault();
        const form = e.target;
        const formData = new FormData(form);
        const response = fetch("http://127.0.0.1:5000/api/analyze_sentiment",{
            method: form.method, // *GET, POST, PUT, DELETE, etc.
            mode: "cors", // no-cors, *cors, same-origin
            cache: "no-store", // *default, no-cache, reload, force-cache, only-if-cached
            credentials: "same-origin", // include, *same-origin, omit
            body: formData
        });
        const formJson = Object.fromEntries(formData.entries());
        console.log(formJson);
    }
      
    return(
        <div>
            <form method="post" onSubmit={handleSubmit}>
            <label htmlFor="search" className="block text-large font-large leading-6 text-white">How is your mood?</label>
            <div className="mt-2">
              <textarea id="search" name="search_query" rows="2" className={`${styles.searchBox} border-white focus:border-[#7c3aed] rounded`}></textarea>
            </div>
            <button type="submit" className="bg-violet-500 hover:bg-indigo-400 text-white font-semibold px-6 py-3 rounded-md">
                Show Recommendations
            </button>
            </form>
        </div>
    )
}

export default SearchBox