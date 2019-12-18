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
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
// reactstrap components
import { Button, Form, Input, Container, Row, Col } from "reactstrap";
import { Text } from 'react-konva';
import "../../../node_modules/react-datepicker/dist/react-datepicker.css"
// core components
import BlackNavbar from "components/Navbars/BlackNavbar.js";

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
        <BlackNavbar />
        <div
          className="page-header"
          data-parallax={true}
          style={{
            backgroundColor:'rgba(255,255,255,1)',
          }}
        >
            <Container style={{display:'flex',flex:1,flexDirection:'column'}}>
              <React.Fragment>
                <Typography variant="h6" gutterBottom>
                  Map Address
                </Typography>
                <Grid container spacing={3}>
                  <Grid item xs={12}>
                    <TextField
                      required
                      id="streetName"
                      name="streetName"
                      label="Street name"
                      fullWidth
                      autoComplete="Rua"
                    />
                  </Grid>
                  <Grid item xs={6} sm={3}>
                      <TextField
                      required
                      id="beginingX"
                      name="beginingX"
                      label="X coord to start"
                      fullWidth
                      autoComplete="0"
                      />
                  </Grid>
                  <Grid item xs={6} sm={3}>
                      <TextField
                      required
                      id="beginingY"
                      name="beginingY"
                      label="Y coord to start"
                      fullWidth
                      autoComplete="0"
                      />
                  </Grid>
                  <Grid item xs={6} sm={3}>
                      <TextField
                      required
                      id="endingX"
                      name="endingX"
                      label="X coord to end"
                      fullWidth
                      autoComplete="1000"
                      />
                  </Grid>
                  <Grid item xs={6} sm={3}>
                      <TextField
                      required
                      id="endingY"
                      name="endingY"
                      label="Y coord to end"
                      fullWidth
                      autoComplete="100"
                      />
                  </Grid>
                  <Grid item xs={12}>
                    <TextField
                      required
                      id="city"
                      name="city"
                      label="City"
                      fullWidth
                      autoComplete="Cidade "
                    />
                  </Grid>
                </Grid>
              </React.Fragment>
            </Container>
        </div>
    </>
    )
  }
}

export default Admin;
