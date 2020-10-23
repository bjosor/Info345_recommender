import React from 'react';
import Select from 'react-select';
import recipeList from '../data/recipedata.json';


const searchList = recipeList.map(
  ({ recipe_name }) => {
    return{ 
     value: recipe_name, 
     label: recipe_name 
    }
   }
  );  

export default class SearchBar extends React.Component{

  constructor (props){
    super(props)
    this.state = {
     selectedOption: null,
    }
  }


     // code to make something happen after selecting an option
  
    render(){
     return (
     <div>
      <Select
        options={searchList}
        onChange={selectedOption => {
          this.setState({ selectedOption })
          // code to make something happen after selecting an option
         }}
        placeholder= "Search..."
        openMenuOnClick={false}
      />
     </div>)
    }
   }