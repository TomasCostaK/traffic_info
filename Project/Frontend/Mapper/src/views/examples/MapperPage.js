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
import map_data_json from "../../data/Mapdata"
import { Stage, Layer, Star,Line,Circle, Text, Image,Rect } from 'react-konva';
// reactstrap components
import { Button, Form, Input, Container, Row, Col } from "reactstrap";
import useImage from 'use-image';
import ReactSearchBox from 'react-search-box'
// core components
import BlackNavbar from "components/Navbars/BlackNavbar.js";

let window_height = 350;
let window_width = 700;
//Ter em conta o zooming distance na width do stroke das estradas e nao so so seu tamanho
var map_data;

const API = '192.168.160.237:8000/';
const DEFAULT_QUERY = 'info_street/';

const PoliceImage = (begx,begy) => {
  const [image] = useImage('../../assets/img/car.jpg');
  return <Image image={image} 
  x = {begx+220}
  y = {begy+40}
  height = {30}
  width = {30}
  />;
};


class RegisterPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      zooming_distance : 7,
      hits: [],
      loading_map:true,
      car_trecho:null,
      car_plate:'',
      time: Date.now(),
      dataSource: [],
      streets : [
        {
          key: 'Porto',
          value: 'Porto',
        },
        {
          key: 'Ilhavo',
          value: 'Ilhavo',
        },
        {
          key: 'Roma',
          value: 'Roma',
        },
      ],
      street : 'Ilhavo',
    };
  }

  componentDidMount() {
    this.interval = setInterval(() => this.setState({ time: Date.now(), loading_map:false } && this.getData()), 2000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  draw_street(searching_car,begx, begy, endx, endy, traffic,direction,police){
    var delta_x,delta_y,points
    delta_x = endx - begx
    delta_y = endy - begy
    points = []
    var street_distance = 4;
    var strWidth = 5;

    if (searching_car){
      var strWidth = 1;
    }

    if (direction){
      points = [0,0,delta_x, delta_y]
      //traffic = "green"
    } else {
      points = [!(delta_x)*street_distance, !(delta_y)*street_distance,delta_x+!(delta_x)*street_distance,delta_y+!(delta_y)*street_distance]
      if (delta_x !== 0 && delta_y !== 0){
        points = [0,street_distance,delta_x,delta_y+street_distance]
      }
      //traffic = "yellow"
    }
    return (
    <>
      <Line 
        x = {begx+220}
        y = {begy+40}
        points={points}
        stroke = {traffic}
        strokeWidth = {strWidth}
      />
      
      {/*this.renderPoints(begx,begy,endx,endy)*/}
    </>
    )
  }

  //Conseguimos fazer tambem uma bola no final
  renderBlock(begx,begy,traffic){
    if(traffic=="white"){
      return <Circle x={begx+220} y={begy+40} radius={6} fill="pink" />

    }
           
  }

  renderPoints(begx,begy,endx,endy,traffic){
    return <>
      <Circle x={begx+220} y={begy+40} radius={5} fill="white" />
      <Circle x={endx+220} y={endy+40} radius={5} fill="white" />
    </>       
  }

  analyse_traffic(congestion){
    if (congestion.toLowerCase() == "medium") {
      return "rgba(245, 229, 27, 1)"
    } 
    else if (congestion.toLowerCase() == "congested"){
      return "rgba(242, 121, 53, 1)" //orange
    }
    else if(congestion.toLowerCase() == "blocked") {
      return "rgba(46, 49, 49, 1)"
    }
    else{
      return "rgba(255,255,255,1)"
    }
  }

  getData(){
    console.log("Making request to info_street: " + 'http://192.168.160.237:8000/info_street/'+this.state.street)
    fetch('http://192.168.160.237:8000/info_street/'+this.state.street, { headers: {'Content-Type': 'application/json'}}).
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

  fill_map = () =>{
    map_data = this.state.dataSource
    //map_data = map_data_json
    const lines = []
    /*
      Quando pesquisamos e se o trecho nao estiver a nulo, estamos a desenhar um mapa de procura e entao,
      precisamos de diminuir thickness das outras ruas e mostrar onde se situa o carro
      caso queiramos sair da view -> colocar trecho a nulo e voltamos a um mapa normal
    */
    var opt = this.state.car_trecho != null
    for (let index = 0; index < map_data.length; index++) {
      const trecho = map_data[index];
      var traffic = this.analyse_traffic(trecho.transit_type)
      //Por isto num array? E dar push do return inteiro
      if(trecho.police){
        traffic = "rgba(0, 181, 204, 1)"
      }
      //console.log("TrechoID :" + trecho.id + ", carID: " + this.state.car_trecho)
      if (opt) {
        if (this.state.car_trecho==trecho.id) {
          lines.push( this.draw_street(false,trecho.beginning_coords_x/this.state.zooming_distance, trecho.beginning_coords_y/this.state.zooming_distance, trecho.ending_coords_x/this.state.zooming_distance, trecho.ending_coords_y/this.state.zooming_distance, traffic , trecho.actual_direction, trecho.police))
        } else {
          lines.push( this.draw_street(true,trecho.beginning_coords_x/this.state.zooming_distance, trecho.beginning_coords_y/this.state.zooming_distance, trecho.ending_coords_x/this.state.zooming_distance, trecho.ending_coords_y/this.state.zooming_distance, traffic , trecho.actual_direction, trecho.police))
        }
      } else {
        lines.push( this.draw_street(false,trecho.beginning_coords_x/this.state.zooming_distance, trecho.beginning_coords_y/this.state.zooming_distance, trecho.ending_coords_x/this.state.zooming_distance, trecho.ending_coords_y/this.state.zooming_distance, traffic , trecho.actual_direction, trecho.police))
      }
    }

    return ( lines )

  }

  searchPlate = (plate) => {
    console.log("New plate:" + plate)
  }

  changeZoom(flag){
    if(flag){
      this.setState({
        zooming_distance : this.state.zooming_distance + 1
      })
    }else{
      this.setState({
        zooming_distance : this.state.zooming_distance - 1
      })
    }
  }

  changeStreet = async (text) =>{
    console.log(text)
    await this.setState({
      street: text.key,
      car_trecho:37
    })
    this.getData();
  }

  render() {
    return (
      <>
        <BlackNavbar />
        <div
          className=""
          data-parallax={true}
          style={{
            marginTop:80,
            backgroundColor:'rgba(0,0,0,0)',
          }}
        >
          <div className="" />
          <Row>
          <Container style={{flex:8}}>
            <Row style={{alignContent:'center',justifyContent:'center',border:10,borderColor:'rgba(0,0,0,0.75)'}}>
              <div style={{padding:20}}>
                <Row style={{color:'black',alignContent:'space-between',justifyContent:'space-between'}}>
                <Text style={{color:'rgba(0,0,0,0.75)', fontWeight:'bold', fontSize:25}}>Map Analysis for:  </Text>
                <ReactSearchBox
                  placeholder="Search street"
                  value="Ilhavo"
                  data={this.state.streets}
                  color={'black'}
                  style={{fontWeight:'bold',width:10}}
                  inputBoxFontColor={'black'}
                  dropDownHoverColor={'rgba(0,255,255,0.1)'}
                  onSelect={record => this.changeStreet(record)}
                />
                <Button style={{marginLeft:10,maxHeight:40}} onClick={() => this.changeZoom(true)}>- Zoom</Button>
                <Button style={{marginLeft:10,maxHeight:40}} onClick={() => this.changeZoom(false)}>+ Zoom</Button>
                </Row>

              </div>
                <Stage style={{backgroundColor:'rgba(0,0,0,0.7)'}} width={window_width} height={window_height}>
                  <Layer  id="map">
                  {/* Aqui desenhamos o mapa */}
                  {this.fill_map()}
                  </Layer>
              </Stage>
            </Row>
          </Container>
          <Container style={{flex:3,marginRight:50,fontWeight:'medium',flexDirection:'column',alignContent:'center',marginTop:150 ,justifyContent:'center'}}>
          <Text style={{color:'black', fontWeight:'bolder', fontSize:20}}>Search Plate:</Text>
          <ReactSearchBox
            placeholder="Search Plate"
            value={this.state.car_plate}
            style={{fontSize:10,fontWeight:'bolder'}}
            data={this.state.car_plate}
            callback={record => console.log(record)}
          />
            <Text style={{color:'black', fontWeight:'bolder', fontSize:20}}>Legenda:</Text>
            <Container style={{flex:1,flexDirection:'column',alignContent:'center',justifyContent:'center',border:10,marginTop:30,borderColor:'rgba(0,0,0,0.75)'}}>
              <Row><Text style={{color:'green', fontWeight:1000, fontSize:18}}>---  </Text><Text style={{color:'black', fontWeight:'bolder', fontSize:15, marginLeft: 10}}>Trânsito Leve</Text></Row>
              <Row><Text style={{color:'yellow', fontWeight:1000, fontSize:18}}>---  </Text><Text style={{color:'black', fontWeight:'bolder', fontSize:15, marginLeft: 10}}>Trânsito Médio</Text></Row>
              <Row><Text style={{color:'red', fontWeight:1000, fontSize:18}}>---  </Text><Text style={{color:'black', fontWeight:'bolder', fontSize:15, marginLeft: 10}}>Trânsito Alto</Text></Row>
              <Row><Text style={{color:'black', fontWeight:1000, fontSize:18}}>---  </Text><Text style={{color:'black', fontWeight:'bolder', fontSize:15, marginLeft: 10}}>Bloqueio</Text></Row>
              <Row><Text style={{color:'blue', fontWeight:1000, fontSize:18}}>---  </Text><Text style={{color:'black', fontWeight:'bolder', fontSize:15, marginLeft: 10}}>Policiamento</Text></Row>
            </Container>
          </Container>
          </Row>
  
        </div>
    </>
    )
  }
}

export default RegisterPage;
