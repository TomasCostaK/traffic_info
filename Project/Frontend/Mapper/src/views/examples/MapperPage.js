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
import React from "react";
import map_data_json from "../../data/Mapdata"
import { render } from 'react-dom';
import { Stage, Layer, Star,Line,Circle, Text } from 'react-konva';
// reactstrap components
import { Button, Form, Input, Container, Row, Col } from "reactstrap";

// core components
import ExamplesNavbar from "components/Navbars/ExamplesNavbar.js";

let window_height = 400;
let window_width = 800;
//Ter em conta o zooming distance na width do stroke das estradas e nao so so seu tamanho
let zooming_distance = 7;

var map_data;

function draw_street(begx, begy, endx, endy, color,direction){
  var delta_x,delta_y,points
  delta_x = endx - begx
  delta_y = endy - begy
  points = []

  if (direction){
    points = [0,0,delta_x, delta_y]
    //color = "green"
  } else {
    points = [!(delta_x)*8, !(delta_y)*8,delta_x+!(delta_x)*8,delta_y+!(delta_y)*8]
    if (delta_x != 0 && delta_y != 0){
      points = [0,8,delta_x-8,delta_y]
    }
    //color = "yellow"
  }
  console.log("Line i will draw: ")
  console.log("Begx: " + begx + ",begy" + begy + ", points: " + points + ", color: " + color)
  return (
    <Line 
      x = {begx+280}
      y = {begy+40}
      points={points}
      stroke = {color}
      strokeWidth = {4}
    />
  )
}

function analyse_traffic(number_cars){
  if (number_cars > 40) {
    return "red"
  } 
  else if (number_cars > 20){
    return "yellow"
  }
  else{
    return "green"
  }
}

function fill_map(){
  //makeRemoteRequest();
  //Adicionar isto assim que tivermos o pedido
  //map_data = map_data_json
  makeRemoteRequest();
  console.log(map_data);
  const lines = []

  for (let index = 0; index < map_data.length; index++) {
    const trecho = map_data[index];
    var traffic = analyse_traffic(trecho.number_cars)
    console.log(trecho)
    //Por isto num array? E dar push do return inteiro
    lines.push( draw_street(trecho.beginning_coords_x/zooming_distance, trecho.beginning_coords_y/zooming_distance, trecho.ending_coords_x/zooming_distance, trecho.ending_coords_y/zooming_distance, traffic , trecho.actual_direction))
  }

  return ( lines )

}

function makeRemoteRequest(){
    console.log("Here");
    return fetch('127.0.0.1:3000/info_street/')
    .then ( (response) => response.json() )
    .then ( (responseJson) =>{
    
    map_data = responseJson;
    console.log(responseJson);

    })
  .catch((error) => {
    console.log(error);
  });
  
}

function RegisterPage() {
  document.documentElement.classList.remove("nav-open");
  React.useEffect(() => {
    document.body.classList.add("register-page");
    return function cleanup() {
      document.body.classList.remove("register-page");
    };
  });
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
            <div style={{padding:20}}>
              <Text style={{color:'white', fontWeight:'bold', fontSize:30}}>Map Analysis for: Espinho</Text>
            </div>
            <Stage width={window_width} height={window_height}>
                <Layer id="map">
                
                {/* Aqui desenhamos o mapa */}
                {fill_map()}

                </Layer>
            </Stage>
          </Row>
        </Container>

      </div>
    </>
  );
}

export default RegisterPage;
