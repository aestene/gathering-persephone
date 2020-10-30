import logo from './logo.svg';
import './App.css';
import React, { Component} from 'react';
import MapContainer from './components/MapContainer'
import WeatherContainer from './components/WeatherForecastComponent' 

export default class App extends Component{
    
    render(){
        return (
            <div>
                <WeatherContainer />
                <MapContainer/>
            </div>
        );
    }
}