import React, { useState } from 'react';

export default function TopBar(props){

    return (
        <div className='TopBar'>
            <button>profile</button>
            {props.loggedIn ? <button onClick={props.logout}>logout</button> : null}
        </div>
    );
}