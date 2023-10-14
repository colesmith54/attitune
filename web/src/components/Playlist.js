import React, { useContext,useState ,useEffect} from 'react'
import {Link,useNavigate, useLocation} from "react-router-dom"
import { Card } from 'react-bootstrap'; 



const Playlist = () =>{
const playlist_data=[
    {
      "album_image": "image_url_1",
      "artist_names": "Artist 1",
      "song_duration": "3:45",
      "song_name": "Song 1",
      "song_uri": "spotify:track:12345"
    },
    {
      "album_image": "image_url_2",
      "artist_names": "Artist 2",
      "song_duration": "4:15",
      "song_name": "Song 2",
      "song_uri": "spotify:track:67890"
    },
  ]


    return (
       <div>
       {Object.keys(playlist_data).length > 0 && (
        <div className="playlist">
          {playlist_data.items.map((item, index) => {
            return (
              <React.Fragment key={index}>
                <Card style={{ width: '18rem' }}>
               
                  <Card.Body>
                    <Card.Title>{item.song_name}</Card.Title>
                    <Card.Text>
                      <small>By {item.artist_names}</small>
                    </Card.Text>
                  </Card.Body>
                </Card>
              </React.Fragment>
            );
          })}
        </div>
      )}
    </div>
    );
};
export default Playlist;