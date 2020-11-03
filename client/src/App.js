import React, { Component } from 'react';
import Search from './pages/Search';
import './App.css';
import Login from './pages/Login';
import ServerConnection from './Serverconnection';
import TopBar from './components/TopBar'

class App extends Component{
  constructor(props){
    super(props)
    this.state = {
      loggedIn: false,
      id: null
    }

    this.server = new ServerConnection('localhost')

    this.getLogin = this.getLogin.bind(this);
    this.logout = this.logout.bind(this);
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

  //TODO
  switchPage(page){
    if (page === 'search'){
      console.log('Woop')
    }
  }

  logout(){
    this.setState({
      loggedIn: false,
      id : null
    })
  }

  render(){
    return (
      <div className="App">
          <TopBar logout={this.logout} loggedIn={this.state.loggedIn}/>
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
