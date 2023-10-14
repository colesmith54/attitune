'use client';
import { useState, useEffect } from 'react';
import Iframe from 'react-iframe';
import styles from '../app/styles/components/iframePopup.module.scss';
import Cross from '../app/svgs/circle-xmark-regular.svg'


function IframePopup({ url }) {
  const [visible, setVisible] = useState(false);  // Visibility state inside the IframePopup

  useEffect(() => {
    if (visible) {
      document.body.classList.add('iframe-active');
    } else {
      document.body.classList.remove('iframe-active');
    }

    return () => {
      document.body.classList.remove('iframe-active');
    };
  }, [visible]);

  return (
    <>
      <button onClick={() => setVisible(true)}>Show Iframe</button>

      {visible && (
        <div className={styles['iframe-overlay']}>
          <button className={styles['close-button']} onClick={() => setVisible(false)}><Cross /></button>
          <Iframe url={url}
                  width="640px"
                  height="320px"
                  className={styles['centered-iframe']}
                  display="block"
                  position="relative"/>
        </div>
      )}
    </>
  );
}

export default IframePopup;
