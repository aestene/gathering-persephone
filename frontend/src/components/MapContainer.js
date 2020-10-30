import React, { Component} from 'react';
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';

const mapStyles = {
  width: '100%',
  height: '100%',
};

export class MapContainer extends Component{
    constructor(props) {
      super(props)
console.log("DFDF" + props.position)
this.state = {}
if (props.position)
      this.state.stores = [{ latitude: this.props.position.coords.latitude, longitude: this.props.position.coords.longitude}]
      }
    
    displayMarkers = () => {
      console.log("MAR" + this.state.stores)
      if (this.state.stores)
      return this.state.stores.map((store, index) => {   
        console.log("MARMAR" + store)
        return <Marker key={index} id={index} position={{
         lat: store.coords.latitude,
         lng: store.coords.longitude
       }}
       onClick={() => console.log("Should display something")} />
      })
    }

    render() {
        return (
          <Map
            google={this.props.google}
            zoom={8}
            style={mapStyles}
            initialCenter={{ lat: 48.00, lng: -122.176}}
          >
            {this.displayMarkers()}
          </Map>
        );
      }
}

export default GoogleApiWrapper({
  apiKey: process.env.GOOGLE_API_KEY 
})(MapContainer);