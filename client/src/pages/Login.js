import React, { useState } from 'react';

export default function Login(props){
    const [id, setId] = useState(null);
    console.log('Login comp')

    return (
        <div className='login'>
            <input type='text' onChange={(event) => {setId(event.target.value)}}></input>
            <button onClick={() => (props.getLogin(id))}>Login</button>
        </div>
    );
}