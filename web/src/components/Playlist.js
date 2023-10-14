'use client';
import React, { useContext,useState ,useEffect} from 'react'


const Playlist = ({ playlistData }) =>{
function millisecondsToMinutes(milliseconds) {
    const minutes = Math.floor(milliseconds / 60000);
    const seconds = ((milliseconds % 60000) / 1000).toFixed(0);
    
    return `${minutes}:${(seconds < 10 ? '0' : '')}${seconds}`;
    }
   
    const playlist_data = playlistData ?? [{"_id": "265Anh9hGoozFigjUVLUeD", "album_image": "https://i.scdn.co/image/ab67616d0000b273280a44b1caee9f2109602c41",
    "artist_names": ["Paolo Nutini"], "song_duration": 203653, "song_name": "New Shoes", 
   "song_uri": "spotify:track:265Anh9hGoozFigjUVLUeD"},
    {"_id": "51UtgWS4z1eMPuLQOzPtNH", "album_image": "https://i.scdn.co/image/ab67616d0000b27362d0614b5dffca14a302b427", "artist_names": ["311"], 
    "song_duration": 211080, "song_name": "Amber", "song_uri": "spotify:track:51UtgWS4z1eMPuLQOzPtNH"}, {"_id": "312A8WfROSLvZbMDHBUPDp", 
    "album_image": "https://i.scdn.co/image/ab67616d0000b2734bf409ede02e2a4069fd02a8", "artist_names": ["The Streets"],
    "song_duration": 254266, "song_name": "Fit but You Know It", "song_uri": "spotify:track:312A8WfROSLvZbMDHBUPDp"},
   
    {"_id": "1FSWSs9CL01RCYxXtm08Rf", "album_image": "https://i.scdn.co/image/ab67616d0000b273ff2057b7343d2233451ff8e7", "artist_names": 
    ["Olly Murs"], "song_duration": 202226, "song_name": "Dance with Me Tonight", "song_uri": "spotify:track:1FSWSs9CL01RCYxXtm08Rf"}];
    
    return (
    <div className="overflow-x-auto">
    <table className="min-w-full bg-gradient-to-r from-gray-900 to-indigo-700">
    <thead>
      <tr>
        <th className="px-2 py-4 whitespace-nowrap text-left">
          #
        </th>
        <th className="px-2 py-4 whitespace-nowrap text-left">
          Title
        </th>
        <th className="px-6 py-4 whitespace-nowrap text-left">
          Artist
        </th>
        <th className="px-6 py-4 whitespace-nowrap text-left">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-clock" viewBox="0 0 16 16">
            <path d="M8 3.5a.5.5 0 0 0-1 0V9a.5.5 0 0 0 .252.434l3.5 2a.5.5 0 0 0 .496-.868L8 8.71V3.5z" fill="white"></path>
            <path d="M8 16A8 8 0 1 0 8 0a8 8 0 0 0 0 16zm7-8A7 7 0 1 1 1 8a7 7 0 0 1 14 0z" fill="white"></path>
            </svg>
        </th>
      </tr>
    </thead>
    <tbody>
      {playlist_data.map((item, index) => (
        <tr key={item._id} className="hover:bg-indigo-600">
          <td className="px-3 py-1 whitespace-nowrap cursor-pointer group">
            {index + 1} {/* Row number */}
           </td>
          <td className="px-3 py-1 whitespace-nowrap">
            <div className="flex items-center space-x-2">
                <img src={item.album_image} alt="album" className="w-10 h-10"/>
                <h2>{item.song_name}</h2>
            </div>
          </td>
          <td className="px-6 py-1 whitespace-nowrap">
            {item.artist_names.slice(0, 2).join(', ')}
          </td>
          <td className="px-6 py-1 whitespace-nowrap">
            {millisecondsToMinutes(item.song_duration)}
          </td>
        </tr>
      ))}
    </tbody>
  </table>
</div>

    );
      
};
export default Playlist;