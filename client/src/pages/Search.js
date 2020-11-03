import React, { useState } from 'react';
import Select from 'react-select';

export default function Search(props){
    return (
        <Search 
        options={props.data} /> 
    );
}