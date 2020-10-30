import logo from './logo.svg';
import './App.css';
import React, { Component} from 'react';
import MapContainer from './components/MapContainer' 


export default class App extends Component{
    position = null
    constructor(props) {
        super(props)
        this.state = {}
      }

      componentDidMount() {
          const that = this
        navigator.geolocation.getCurrentPosition(
            function(position) {
              that.setState({position: position})
              console.error(position)
            },
            function(error) {
              console.error("Error Code = " + error.code + " - " + error.message);
            }
          );
      }

    render(){
        console.log("RENDEr" + this.state.position)
        return (
                <MapContainer position = {this.state.position}/>
    
        );
    }
}