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
import "../../../node_modules/react-datepicker/dist/react-datepicker.css"
// core components
import ExamplesNavbar from "components/Navbars/ExamplesNavbar.js";

const API = '192.168.160.237:8000/';
const DEFAULT_QUERY = 'all_streets/';

//Fazer as stats como class independende


class Admin extends Component {

  constructor(props) {
    super(props);
    this.state = {
      dataSource: [],
    };
  }

  //date-format: AAAA-MM-DD

  componentDidMount() {
    //somting in here
  }

  componentWillUnmount() {
    //sumting heya
  }

  getDataStats = () => {
    console.log("Making request to statistics")
    var final_url = '';
    fetch( API + final_url, {  
      method: 'POST',
      headers: {'Content-Type': 'application/json'} 
    }).
      then(resp => {
        console.log(JSON.stringify(resp.body))
        return resp;
      })
      .then(data => {this.setState({
        //dataSourceStats : [data]
      })
    });
  }

  render() {
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
            <Container style={{display:'flex',flex:1,flexDirection:'column'}}>
                <Row>
                    <Text style={{color:'white',fontWeight:'bolder'}}>ADMIN CHANGING STREETS</Text>
                </Row>
            </Container>
        </div>
    </>
    )
  }
}

export default Admin;
