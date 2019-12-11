/*!

=========================================================
* Paper Kit React - v1.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/paper-kit-react

* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/paper-kit-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React, { Component } from "react";
// reactstrap components
import { Button, Form, Input, Container, Row, Col } from "reactstrap";
import { Text } from 'react-konva';

// core components
import ExamplesNavbar from "components/Navbars/ExamplesNavbar.js";

const API = '192.168.160.237:8000/';
const DEFAULT_QUERY = 'info_street/';


class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      zooming_distance : 6,
      hits: [],
      time: Date.now(),
      dataSource: [],
    };
  }

  componentDidMount() {
    this.interval = setInterval(() => this.setState({ time: Date.now() } && this.getData()), 5000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  getData(){
    console.log("Making request to info_street")
    fetch('http://192.168.160.237:8000/info_street/', { headers: {'Content-Type': 'application/json'}}).
      then(resp => resp.json()).
      then(responseData => {
        console.log(responseData);
        return responseData;
      })
      .then(data => {this.setState({
        dataSource : data
      })
    });
  }

  render() {
    const { hits } = this.state;
    return (
      <>
        <ExamplesNavbar />
        <div
          className="page-header"
          data-parallax={true}
          style={{
            backgroundColor:'rgba(0,0,0,.85)',
          }}
        >
          <div className="" />
          <Container>
            <Row style={{alignContent:'center',justifyContent:'center',border:10,borderColor:'white'}}> 
                <Text style={{color:'white', fontWeight:'bold', fontSize:30}}>Analytics for streets in: Espinho</Text>
            </Row>
          </Container>
  
        </div>
    </>
    )
  }
}

export default Dashboard;
