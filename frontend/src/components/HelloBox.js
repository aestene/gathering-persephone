import React, { Component} from 'react';

export class HelloBox extends Component{
    constructor(props) {
      super(props);
    }

    render() {
        return (
          
        );
      }
}

export default GoogleApiWrapper({
  apiKey: process.env.GOOGLE_API_KEY 
})(MapContainer);