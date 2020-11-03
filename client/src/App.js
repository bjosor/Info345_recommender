import React, { Component } from 'react';
import Search from './pages/Search';
import './App.css';
import Login from './pages/Login';
import ServerConnection from './Serverconnection';

class App extends Component{
  constructor(props){
    super(props)
    this.state = {
      loggedIn: false
    }

    this.server = new ServerConnection('localhost')

    this.getLogin = this.getLogin.bind(this);
  }

  componentDidUpdate(prevProps, prevState){
    console.log('update')
    if(prevState.id !== this.state.id) {
      this.server.apiCallSingle('http://localhost:8080/request?id=' + this.state.id)
      .then((response) => {this.setState({data: response})})
    }
  }

  getLogin(id){
    console.log(id)
    if(id !== null){
      this.setState({
        loggedIn: true,
        id : id
      })
    } else {
      console.log('No login id provided')
    }

  }

  render(){
    return (
      <div className="App">
          {this.state.loggedIn ? 
          <Search 
          className='searchbox'
          options={this.state.data} /> 
          :
          <Login getLogin={this.getLogin}/>}
          
      </div>
    );
  }

}



export default App;
