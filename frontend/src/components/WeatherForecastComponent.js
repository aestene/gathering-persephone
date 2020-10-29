import React from 'react';
import './_style.scss'
import AccessTimeIcon from '@material-ui/icons/AccessTime';
import CloudIcon from '@material-ui/icons/Cloud';
import WbSunnyIcon from '@material-ui/icons/WbSunny';
import GrainIcon from '@material-ui/icons/Grain';
import skyIcon from '../icons/sky.jpg'

export default function BasicTable() {

  return (
    <table className="weather-forecast-table" background={skyIcon} border='1'>
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
        <td className="cloud_icon">
          <div><CloudIcon style={{ color: 'gray'}}/></div>
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
  );
}

