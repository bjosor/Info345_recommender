import React, { Component } from 'react';
import './App.css';
import ServerConnection from './Serverconnection';

class App extends Component{
  constructor(props){
    super(props)
    this.state = {}

    this.server = new ServerConnection('localhost')
  }

  componentDidMount(){
    console.log('cake')
    this.server.apiCallSingle('http://localhost:8080/request')
  }

  render(){
    return (
      <div className="App">
        <header className="App-header">
          <p className='woop'>
            Fabulous Page 2.0
          </p>
          <p className='woop'>
            Fabulous Page 2.0
          </p>
          <p className='woop'>
            Fabulous Page 2.0
          </p>
          <p className='woop'>
            Fabulous Page 2.0
          </p>
          <p className='woop'>
            Fabulous Page 2.0
          </p>
          <p className='woop'>
            Fabulous Page 2.0
          </p>
        </header>
      </div>
    );
  }

}

export default App;
