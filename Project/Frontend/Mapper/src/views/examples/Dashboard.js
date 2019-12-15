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
import moment from 'moment';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';
import ReactSearchBox from 'react-search-box'
import DatePicker from "react-datepicker";
import "../../../node_modules/react-datepicker/dist/react-datepicker.css"
// core components
import ExamplesNavbar from "components/Navbars/ExamplesNavbar.js";

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

  constructor(props) {
    super(props);
    this.state = {
      hits: [],
      street_name: '',
      street_id: 1,
      begin_date: moment().format('YYYY-MM-DD'),
      end_date: moment().format('YYYY-MM-DD'),
      begin_date_cal: new Date(),
      end_date_cal: new Date(),
      dayofweek:'',
      dataSource: [],
      dataSourceStats: [{
        "name": "Rua Tenente Joaquim Lopes Craveiro", 
        "transit_count": 0, 
        "road_block": {"total_time": 0, "times": 0},
        "total_accident": []
      }],
      options : ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    };
  }

  //date-format: AAAA-MM-DD

  componentDidMount() {
    this.getData()
  }

  componentWillUnmount() {
    //sumting heya
  }

  handleChangeStart = async date => {
    await this.setState({
      begin_date: moment(date).format('YYYY-MM-DD'),
      begin_date_cal: date
    });
    this.getDataStats()
  };

  handleChangeEnd = async date => {
    await this.setState({
      end_date: moment(date).format('YYYY-MM-DD'),
      end_date_cal: date
    });
    this.getDataStats()
  };

  getData = () => {
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

  getDataStats = () => {
    console.log("Making request to statistics")
    var final_url = this.state.street_id + '/' + this.state.begin_date + '/' + this.state.end_date + '/' + this.state.dayofweek;
    console.log(API + STATS_QUERY + final_url)
    fetch( API + STATS_QUERY + final_url, {  
      method: 'GET',
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

  changeStreetDisplayed(response) {
    this.setState({
      street_name: response.value,
      street_id : response.key
    })
    this.getDataStats()
  }

  changeDay = async (day) => {
    await this.setState({
      dayofweek : day.value
    })
    this.getDataStats();
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
              data={this.state.dataSource}
              color={'black'}
              style={{fontWeight:'bold',width:40}}
              inputBoxFontColor={'black'}
              dropDownHoverColor={'rgba(0,255,255,0.3)'}
              onSelect={record => this.changeStreetDisplayed(record)}
            />
            <Row style={{flex:1, alignContent:'space-between',justifyContent:'space-between'}}>
              <Container style={{flex:1, alignContent:'center',justifyContent:'center'}}>
                <Text style={{color:'white', fontSize:20, marginTop:5, fontWeight:'bolder'}}>Start Date: </Text>
                <DatePicker
                  selected={this.state.begin_date_cal}
                  onChange={this.handleChangeStart}
                />
              </Container>
              <Container style={{flex:1, alignContent:'center',justifyContent:'center'}}>
                <Text style={{color:'white', fontSize:20, marginTop:5, fontWeight:'bolder'}}>End Date: </Text>
                <DatePicker
                  selected={this.state.end_date_cal}
                  onChange={this.handleChangeEnd}
                />
              </Container>
              <Dropdown style={{marginRight:40}} options={this.state.options} onChange={(day) =>this.changeDay(day)} value={this.state.dayofweek} placeholder="Select a day" />
            </Row>
        <Text style={{color:'white', fontWeight:'bold', marginTop:80, textAlign:'center',fontSize:30}}>{this.state.street_name}</Text>
            <div style={{display:'flex', flexDirection:'row' , justifyContent:'space-between',alignContent:'space-between'}}>
              <Stats style={{flex:1}} stat_name="Nº of accidents" number={this.state.dataSourceStats[0].total_accident}/>
              <Stats style={{flex:1}} stat_name="Roadblock total time" number={this.state.dataSourceStats[0].road_block.total_time}/>
              <Stats style={{flex:1}} stat_name="Nº of roadblocks" number={this.state.dataSourceStats[0].road_block.times}/>
              <Stats style={{flex:1}} stat_name="Transit Count" number={this.state.dataSourceStats[0].transit_count}/>

            </div>
            </Container>
        </div>
    </>
    )
  }
}

export default Dashboard;
