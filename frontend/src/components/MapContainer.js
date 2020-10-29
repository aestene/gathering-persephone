import React, { Component} from 'react';
import { Map, GoogleApiWrapper, Marker } from 'google-maps-react';

const mapStyles = {
  width: '100%',
  height: '100%',
};

export class MapContainer extends Component{
    constructor(props) {
      super(props);

      this.state = {
        stores: [{ latitude: 48.00, longitude: -122.176}]
      }
    }
    
    displayMarkers = () => {
      return this.state.stores.map((store, index) => {
        return <Marker key={index} id={index} position={{
         lat: store.latitude,
         lng: store.longitude
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