import React, { useEffect, useState } from 'react';
import './_styles.scss'
import CloudIcon from '@material-ui/icons/Cloud';
import WbSunnyIcon from '@material-ui/icons/WbSunny';
import GrainIcon from '@material-ui/icons/Grain';
import skyIcon from '../icons/sky.jpg'
import axios from 'axios'

export default function BasicTable() {
  const [forecast, setForecast] = useState({})


  const getAndSetData = () => {
    getForecast()
  }

  useEffect(() => {
    getAndSetData().then((response) => {setResponse(response)})
  }, [forecast])


  const getForecast = async () => {
    const requestConfig = {
      responseType: 'application/json',
      params: {latitude: 10, longitude: 15}
    }

    await axios.get("http://localhost:5000/persephone/weather/compact-forecast", requestConfig)
  }

  const setResponse = (response) => {
    setForecast(JSON.parse(response.data))
  }



  return (
    <div>
      <table className="weather-forecast-table" border='1'>
        <h3 className="header">Weather Forecast //Place Name//</h3>
      <tr>
        <td className="weather-forecast-label">Hours</td>
        {forecast.map((hour) => {
          return (
          <td className="weather-forecast-values">{hour[0].details.air_temperature}</td>
          )
        })}
      </tr>
      
      <tr>
        <td className="weather-forecast-label">Hours</td>
        <td className="weather-forecast-values">6</td>
        <td className="weather-forecast-values">9</td>
        <td className="weather-forecast-values">12</td>
        <td className="weather-forecast-values">15</td>
      </tr>
      <tr>
        <td className="weather-forecast-label"></td>
        <td className="weather-forecast-values"><CloudIcon style={{ color: 'gray'}}/></td>
        <td className="weather-forecast-values"><WbSunnyIcon style={{ color: '#e6e600'}}/></td>
        <td className="weather-forecast-values">
          <div className="cloud_icon"><CloudIcon style={{ color: 'gray'}}/></div>
          <div className="sun_icon"> <WbSunnyIcon style={{ color: '#e6e600'}}/></div>
        </td>
        <td className="weather-forecast-values">
          <div className="cloud_icon"><CloudIcon style={{ color: 'gray'}}/></div>
          <div className="rain_icon"> <GrainIcon style={{ color: '#72bcd4'}}/></div>
        </td>
      </tr>
      <tr>
        <td className="weather-forecast-label">Tempertaure C&#176;</td>
        <td className="weather-forecast-values">10&#176;</td>
        <td className="weather-forecast-values">12&#176;</td>
        <td className="weather-forecast-values">18&#176;</td>
        <td className="weather-forecast-values">6&#176;</td>
      </tr>
      <tr>
        <td className="weather-forecast-label">Rain (mm)</td>
        <td className="weather-forecast-values">10</td>
        <td className="weather-forecast-values">12</td>
        <td className="weather-forecast-values">18</td>
        <td className="weather-forecast-values">6</td>
      </tr>
      <tr>
      <td className="weather-forecast-label">Wind (kt)</td>
        <td className="weather-forecast-values">5</td>
        <td className="weather-forecast-values">9</td>
        <td className="weather-forecast-values">7</td>
        <td className="weather-forecast-values">10</td>
      </tr>
  </table>
    </div>
  );
}

