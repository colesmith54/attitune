'use client';
import React, { useContext,useState ,useEffect} from 'react'
import { Card } from 'react-bootstrap'; 



const Playlist = () =>{
const playlist_data=[{"_id": "265Anh9hGoozFigjUVLUeD", "album_image": "https://i.scdn.co/image/ab67616d0000b273280a44b1caee9f2109602c41",
    "artist_names": ["Paolo Nutini"], "song_duration": 203653, "song_name": "New Shoes", 
   "song_uri": "spotify:track:265Anh9hGoozFigjUVLUeD"},
    {"_id": "51UtgWS4z1eMPuLQOzPtNH", "album_image": "https://i.scdn.co/image/ab67616d0000b27362d0614b5dffca14a302b427", "artist_names": ["311"], 
    "song_duration": 211080, "song_name": "Amber", "song_uri": "spotify:track:51UtgWS4z1eMPuLQOzPtNH"}, {"_id": "312A8WfROSLvZbMDHBUPDp", 
    "album_image": "https://i.scdn.co/image/ab67616d0000b2734bf409ede02e2a4069fd02a8", "artist_names": ["The Streets"],
    "song_duration": 254266, "song_name": "Fit but You Know It", "song_uri": "spotify:track:312A8WfROSLvZbMDHBUPDp"},
   
    {"_id": "1FSWSs9CL01RCYxXtm08Rf", "album_image": "https://i.scdn.co/image/ab67616d0000b273ff2057b7343d2233451ff8e7", "artist_names": 
    ["Olly Murs"], "song_duration": 202226, "song_name": "Dance with Me Tonight", "song_uri": "spotify:track:1FSWSs9CL01RCYxXtm08Rf"}];



    return (
       <div classname="container">
        <div classname="row">
            <div className="col-md-6">
            {/* This is the empty column */}
            </div>
            {Object.keys(playlist_data).length > 0 && (
                <div className="playlist">
                {playlist_data.map((item, index) => {
                    return (
                    <React.Fragment key={index}>
                        <Card class="bg-gradient-to-r from-indigo-500 ..." style={{ width: '18rem' }}>
                        <Card.Body>
                        <div className="flex items-center space-x-2"> 
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-music-note" viewBox="0 0 16 16">
                            <path d="M9 13c0 1.105-1.12 2-2.5 2S4 14.105 4 13s1.12-2 2.5-2 2.5.895 2.5 2z"/>
                            <path fill-rule="evenodd" d="M9 3v10H8V3h1z"/>
                            <path d="M8 2.82a1 1 0 0 1 .804-.98l3-.6A1 1 0 0 1 13 2.22V4L8 5V2.82z"/>
                            </svg>
                            <Card.Title class="text-lg font-semibold text-white font-helvetica">{item.song_name}</Card.Title>
                        </div>
                        <Card.Text>
                            <small className="mt-3 ml-6" style={{ color: 'white' }}>By {item.artist_names.slice(0, 2).join(', ')}</small>
                        </Card.Text>
                            
                        </Card.Body>
                        </Card>
                    </React.Fragment>
                    );
                })}
                </div>
            )}
      </div>
    </div>
    );
};
export default Playlist;