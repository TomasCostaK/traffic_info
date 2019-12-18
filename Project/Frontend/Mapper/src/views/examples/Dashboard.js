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
import { Bar, Line, defaults } from 'react-chartjs-2';
import DatePicker from "react-datepicker";
import "../../../node_modules/react-datepicker/dist/react-datepicker.css"
// core components
import BlackNavbar from "components/Navbars/BlackNavbar.js";

const API = 'http://192.168.160.237:8000/';
const DEFAULT_QUERY = 'all_streets/';
const ALL_CITIES = 'available_cities/';
const STATS_QUERY = 'statistics/';
const GRAPH_STATS = 'charts/';


//Fazer as stats como class independende
class Stats extends React.Component {
  render() {
    return ( 
        <div>
          <h3 style={{color:'rgba(0,0,0,0.6)', fontWeight:'bolder', fontSize:20}}>{this.props.stat_name}</h3>
          <h4 style={{color:'rgba(0,0,0,0.6)', fontWeight:'bolder', textAlign:'center' ,fontSize:22}}> {this.props.number} </h4>
        </div>
    );
  }
}

class Dashboard extends Component {

  constructor(props) {
    super(props);
    this.state = {
      hits: [],
      street_name: "Rua Tenente Joaquim Lopes Craveiro",
      street_id: 1,
      begin_date: moment().format('YYYY-MM-DD'),
      end_date: moment().format('YYYY-MM-DD'),
      begin_date_cal: new Date(),
      end_date_cal: new Date(),
      dayofweek:'',
      dataSource: [],
      labels:[],
      values:[],
      type_chart:{'key':'Accidents','value':'accident'},
      dataSourceStats: [{
        "name": "", 
        "transit_count": 0, 
        "road_block": {"total_time": 0, "times": 0},
        "total_accident": 0
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

  fillStats = (respo) => {
    let dataSourceGraph = {
      //labels: [respo.Days],
      labels: ['2019-01-01','2019-01-02'],
      datasets: [{
          label: '# of Accidents',
          //data: [respo.ammount],
          data: [1,0],
          backgroundColor: [
            'cyan',
              'cyan',
              'cyan',
              'cyan',
              'cyan',
              'cyan',
        ],
          borderColor: [
              'cyan',
              'cyan',
              'cyan',
              'cyan',
              'cyan',
              'cyan',
          ],
          backgroundColor:'rgba(0,255,255, 0.3)',
          borderWidth: 2
      }]
  }
  return dataSourceGraph;
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
    fetch(API+DEFAULT_QUERY, { headers: {'Content-Type':'application/json'}}).
      then(resp => resp.json()).
      then(rest => {
        console.log("Making request to info_street")
        console.log(rest);
        return rest
      }).
      then(responseData => {
        this.setState({
          dataSource : responseData
        })
      });
  }
  
  /*
  getDataGraph = () => {
    console.log(API+GRAPH_STATS+this.state.type_chart.value+ '/street=' + this.state.street_id +'&start_date=' + this.state.begin_date +' &end_date=' + this.state.end_date +'/')
    fetch(API+GRAPH_STATS+this.state.type_chart.value+'/street=' + this.state.street_id +'&start_date=' + this.state.begin_date +' &end_date=' + this.state.end_date +'/', { headers: {'Content-Type':'application/json'}}).
      then(resp => resp.json()).
      then(rest => {
        return rest
      }).
      then(responseData => {
        this.setState({
          labels : responseData.Days,
          values: responseData.ammount
        })
        this.fillStats(responseData)
      });
  }*/

  getDataStats = () => {
    console.log("Making request to statistics")
    var final_url = this.state.street_id + '/' + this.state.begin_date + '/' + this.state.end_date + '/' + this.state.dayofweek;
    console.log(API + STATS_QUERY + final_url)
    fetch( API + STATS_QUERY + final_url, {  
      headers: {'Content-Type': 'application/json'} 
    })
      .then(results => results.json())
      .then(data => {
        console.log(data)
        this.setState({
        dataSourceStats : [data]
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
    return (
      <>
        <BlackNavbar />
        <div
          className=""
          data-parallax={true}
          style={{
            marginTop:100,
            backgroundColor:'rgba(0,0,0,0)',
            fontWeight:'medium',
          }}
        >
          <Container style={{display:'flex',flex:1,flexDirection:'column',maringTop:50}}>
            <Row style={{alignContent:'center',justifyContent:'center',border:10,borderColor:'white'}}> 
                <Text style={{color:'rgba(0,0,0,0.6)', fontWeight:'bold', fontSize:30}}>Analytics for streets in: Espinho</Text>
            </Row>
            <Text style={{color:'rgba(0,0,0,0.6)', fontSize:13, marginTop:5, fontWeight:'bolder'}}>Street name: </Text>
            <ReactSearchBox
              placeholder="Search street"
              value=""
              data={this.state.dataSource}
              color={'black'}
              style={{fontWeight:'bold',width:40}}
              inputBoxFontColor={'black'}
              dropDownHoverColor={'rgba(0,255,255,0.1)'}
              onSelect={record => this.changeStreetDisplayed(record)}
            />
            
            <Row style={{flex:1, alignContent:'space-between',justifyContent:'space-between'}}>
              <Container style={{flex:1, alignContent:'center',justifyContent:'center'}}>
                <Text style={{color:'rgba(0,0,0,0.6)', fontSize:13, marginTop:5, fontWeight:'bolder'}}>Start Date: </Text>
                <DatePicker
                  selected={this.state.begin_date_cal}
                  onChange={this.handleChangeStart}
                />
              </Container>
              <Container style={{flex:1, alignContent:'center',justifyContent:'center'}}>
                <Text style={{color:'rgba(0,0,0,0.6)', fontSize:13, marginTop:5, fontWeight:'bolder'}}>End Date: </Text>
                <DatePicker
                  selected={this.state.end_date_cal}
                  onChange={this.handleChangeEnd}
                />
              </Container>
              <Container style={{flex:1, alignContent:'center',justifyContent:'center'}}>
                <Text style={{color:'rgba(0,0,0,0.6)', fontSize:13, marginTop:5, fontWeight:'bolder'}}>Week Day: </Text>
                <Dropdown options={this.state.options} onChange={(day) => this.changeDay(day)} value={this.state.dayofweek} placeholder="Select a day" />

              </Container>
            </Row>
        <Text style={{color:'rgba(0,0,0,0.6)', fontWeight:'bold', marginTop:80, textAlign:'center',fontSize:24}}>{this.state.street_name}</Text>
            <div style={{display:'flex', flexDirection:'row' , justifyContent:'space-between',alignContent:'space-between'}}>
              <Stats style={{flex:1}} stat_name="Nº of accidents" number={this.state.dataSourceStats[0].total_accident}/>
              <Stats style={{flex:1}} stat_name="Roadblock total time" number={this.state.dataSourceStats[0].road_block.total_time}/>
              <Stats style={{flex:1}} stat_name="Nº of roadblocks" number={this.state.dataSourceStats[0].road_block.times}/>
              <Stats style={{flex:1}} stat_name="Transit Count" number={this.state.dataSourceStats[0].transit_count}/>

            </div>
            </Container>    
          </div>
          {/* ChartJS */}
          <div>
          <Row style={{alignContent:'center',justifyContent:'center', marginTop:30}}>
          <div
            style={{
              backgroundColor:'rgba(255,255,255,1)',
            }}
          >
            <Line width={1000} height={250} data={(response) => this.fillStats(response)} />
          </div>
          </Row>
        </div>
    </>
    )
  }
}

export default Dashboard;
