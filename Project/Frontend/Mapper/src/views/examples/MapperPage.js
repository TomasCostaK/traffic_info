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

// core components
import BlackNavbar from "components/Navbars/BlackNavbar.js";

let window_height = 650;
let window_width = 850;
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
      zooming_distance : 6,
      hits: [],
      loading_map:true,
      time: Date.now(),
      dataSource: [],
    };
  }

  componentDidMount() {
    this.interval = setInterval(() => this.setState({ time: Date.now(), loading_map:false } && this.getData()), 2000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  draw_street(begx, begy, endx, endy, traffic,direction,police){
    var delta_x,delta_y,points
    delta_x = endx - begx
    delta_y = endy - begy
    points = []
    var street_distance = 7;

    if (direction){
      points = [0,0,delta_x, delta_y]
      //traffic = "green"
    } else {
      points = [!(delta_x)*street_distance, !(delta_y)*street_distance,delta_x+!(delta_x)*street_distance,delta_y+!(delta_y)*street_distance]
      if (delta_x !== 0 && delta_y !== 0){
        points = [0,street_distance,delta_x-street_distance,delta_y]

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
        strokeWidth = {4}
      />
      
      {/*this.renderBlock(begx,begy,traffic)*/}
      {this.renderPoints(begx,begy,endx,endy)}
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
      <Circle x={begx+220} y={begy+40} radius={6} fill="green" />
      <Circle x={endx+220} y={endy+40} radius={6} fill="green" />
    </>       
  }

  analyse_traffic(congestion){
    if (congestion.toLowerCase() == "medium") {
      return "yellow"
    } 
    else if (congestion.toLowerCase() == "congested"){
      return "red"
    }
    else if(congestion.toLowerCase() == "blocked") {
      return "black"
    }
    else{
      return "green"
    }
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

  fill_map(){
    map_data = this.state.dataSource
    //map_data = map_data_json
    const lines = []

    for (let index = 0; index < map_data.length; index++) {
      const trecho = map_data[index];
      var traffic = this.analyse_traffic(trecho.transit_type)
      //Por isto num array? E dar push do return inteiro
      lines.push( this.draw_street(trecho.beginning_coords_x/this.state.zooming_distance, trecho.beginning_coords_y/this.state.zooming_distance, trecho.ending_coords_x/this.state.zooming_distance, trecho.ending_coords_y/this.state.zooming_distance, traffic , trecho.actual_direction, trecho.police))
    }

    return ( lines )

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
          }}
        >
          <div className="" />
          <Container>
            <Row style={{alignContent:'center',justifyContent:'center',border:10,marginTop:30,borderColor:'rgba(0,0,0,0.75)'}}>
              <div style={{padding:20}}>
                <Text style={{color:'rgba(0,0,0,0.75)', fontWeight:'bold', fontSize:30}}>Map Analysis for: Espinho</Text>
                <Button style={{marginLeft:20}} onClick={() => this.changeZoom(true)}>- Zoom</Button>
                <Button onClick={() => this.changeZoom(false)}>+ Zoom</Button>
              </div>
                <Stage style={{backgroundColor:'rgba(0,0,0,0.75)'}} width={window_width} height={window_height}>
                  <Layer  id="map">
                  {/* Aqui desenhamos o mapa */}
                  {this.fill_map()}
                  </Layer>
              </Stage>
            </Row>
          </Container>
  
        </div>
    </>
    )
  }
}

export default RegisterPage;
