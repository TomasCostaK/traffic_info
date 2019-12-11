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
import ReactSearchBox from 'react-search-box'
// core components
import ExamplesNavbar from "components/Navbars/ExamplesNavbar.js";
import { findByLabelText } from "@testing-library/dom";

const API = '192.168.160.237:8000/';
const DEFAULT_QUERY = 'all_streets/';
const STATS_QUERY = 'statistics/';

//Fazer as stats como class independende
class Stats extends React.Component {
  render() {
    return (
        <div>
          <h3 style={{color:'white', fontWeight:'bold', fontSize:20}}>{this.props.stat_name}</h3>
          <h4 style={{color:'white', fontWeight:'bold', textAlign:'center' ,fontSize:20}}> {this.props.number} </h4>
        </div>
    );
  }
}

class Dashboard extends Component {
  data = [
    {
        "key": 1,
        "value": "Rua Tenente Joaquim Lopes Craveiro"
    },
    {
        "key": 2,
        "value": "Rua de Caveiros"
    },
    {
        "key": 3,
        "value": "Rua Romana"
    },
    {
        "key": 4,
        "value": "Travessa da Agoncida"
    },
    {
        "key": 5,
        "value": "Avenida Antonio Henriques"
    },
    {
        "key": 6,
        "value": "Avenida Benjamim Araujo"
    },
    {
        "key": 7,
        "value": "Avenida da Liberdade"
    },
    {
        "key": 8,
        "value": "Avenida da Misericordia"
    },
    {
        "key": 9,
        "value": "Avenida do Brasil"
    },
    {
        "key": 10,
        "value": "Avenida do Vale"
    },
    {
        "key": 11,
        "value": "Avenida do Vale"
    }
]

  constructor(props) {
    super(props);
    this.state = {
      hits: [],
      street_name: '',
      street_id: 1,
      begin_date:'',
      end_date:'',
      dataSource: [],
      dataSourceStats: []
    };
  }

  componentDidMount() {
    //somting in here
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  getData(){
    console.log("Making request to info_street")
    fetch(API+DEFAULT_QUERY, { headers: {'Content-Type': 'application/json'}}).
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

  getDataStats(){
    console.log("Making request to statistics")
    console.log(API+STATS_QUERY)
    fetch(API+STATS_QUERY, { 
      method: 'GET', 
      body: {
        "id":this.state.street_id,
        "begin":this.state.start_date,
        "end":this.state.end_date
      }, 
      headers: {'Content-Type': 'application/json'} 
    }).
      then(resp => resp.json()).
      then(responseData => {
        console.log(responseData);
        return responseData;
      })
      .then(data => {this.setState({
        dataSourceStats : data[0]
      })
    });
  }

  changeStreetDisplayed(response) {
    this.setState({
      street_name: response.value,
      street_id : response.key
    })
    //this.getDataStats()
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
          <Container style={{display:'flex',flex:1,flexDirection:'column'}}>
            <Row style={{alignContent:'center',justifyContent:'center',border:10,borderColor:'white'}}> 
                <Text style={{color:'white', fontWeight:'bold', fontSize:30}}>Analytics for streets in: Espinho</Text>
            </Row>
            <ReactSearchBox
              placeholder="Search street"
              value="Rua Tenente Joaquim Lopes Craveiro"
              style={{width:50}}
              data={this.data}
              color={'black'}
              style={{fontWeight:'bold'}}
              inputBoxFontColor={'black'}
              dropDownHoverColor={'rgba(0,255,255,0.3)'}
              onSelect={record => this.changeStreetDisplayed(record)}
            />
            
        <Text style={{color:'white', fontWeight:'bold', marginTop:80, textAlign:'center',fontSize:30}}>{this.state.street_name}</Text>
            <div style={{display:'flex', flexDirection:'row' , justifyContent:'space-between',alignContent:'space-between'}}>
              <Stats style={{flex:1}} stat_name="Acidentes" number="12"/>
              <Stats style={{flex:1}} stat_name="Roadblock total time" number="0.6h"/>
              <Stats style={{flex:1}} stat_name="Nº of roadblocks" number="2"/>
              <Stats style={{flex:1}} stat_name="Transit Count" number="5"/>

            </div>
            </Container>
        </div>
    </>
    )
  }
}

export default Dashboard;
