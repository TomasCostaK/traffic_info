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

import Konva from 'konva';
import { render } from 'react-dom';
import { Stage, Layer, Star,Line,Circle, Text } from 'react-konva';
// reactstrap components
import { Button, Form, Input, Container, Row, Col } from "reactstrap";

// core components
import ExamplesNavbar from "components/Navbars/ExamplesNavbar.js";

function submitForm(formValue) {
  alert("Login Success")
  if (true){
    window.location.replace('/index');
  }
}

function handleDragStart(e) {
    e.target.setAttrs({
      shadowOffset: {
        x: 15,
        y: 15
      },
      scaleX: 1.1,
      scaleY: 1.1
    });
  };
function handleDragEnd(e) {
    e.target.to({
      duration: 0.5,
      easing: Konva.Easings.ElasticEaseOut,
      scaleX: 1,
      scaleY: 1,
      shadowOffsetX: 5,
      shadowOffsetY: 5
    });
  };

let window_height = 400;
let window_width = 800;

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
          backgroundColor:'black',
        }}
      >
        <div className="" />
        <Container>
          <Row style={{alignContent:'center',justifyContent:'center',border:10,borderColor:'white'}}>
            <Text style={{color:'white', fontWeight:'bold', fontSize:30}}>Map Analysis for: Espinho</Text>
            <Stage width={window_width} height={window_height}>
                <Layer>
                {/* Aqui fazer as linhas (mudar isto para um for e dar draw automatico, mt cancer para ja)*/}
                {/* 1 linha */}
                <Line
                  x={250}
                  y={100}
                  id={1}
                  points={[0, 0, 100, 0]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={350}
                  y={100}
                  points={[0, 0, 100, 0]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={450}
                  y={100}
                  points={[0, 0, 100, 0]}
                  stroke="red"
                  draggable
                  strokeWidth="5"            
                />
                  {/* 2 linha */}
                <Line
                  x={250}
                  y={200}
                  points={[0, 0, 100, 0]}
                  stroke="red"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={350}
                  y={200}
                  points={[0, 0, 100, 0]}
                  stroke="red"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={450}
                  y={200}
                  points={[0, 0, 100, 0]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />
                {/* 3 linha */}

                <Line
                  x={250}
                  y={300}
                  points={[0, 0, 100, 0]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={350}
                  y={300}
                  points={[0, 0, 100, 0]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={450}
                  y={300}
                  points={[0, 0, 100, 0]}
                  stroke="red"
                  draggable
                  strokeWidth="5"            
                />

                {/* Agora fazer as colunas */}
                {/* 1 coluna */}
                <Line
                  x={250}
                  y={100}
                  points={[0, 0, 0, 100]}
                  stroke="red"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={250}
                  y={200}
                  points={[0, 0, 0, 100]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />

                {/* 2 coluna */}
                <Line
                  x={350}
                  y={100}
                  points={[0, 0, 0, 100]}
                  stroke="red"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={350}
                  y={200}
                  points={[0, 0, 0, 100]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />

                {/* 3 coluna */}
                <Line
                  x={450}
                  y={100}
                  points={[0, 0, 0, 100]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={450}
                  y={200}
                  points={[0, 0, 0, 100]}
                  stroke="yellow"
                  draggable
                  strokeWidth="5"            
                />

                {/* 4 coluna */}
                <Line
                  x={550}
                  y={100}
                  points={[0, 0, 0, 100]}
                  stroke="red"
                  draggable
                  strokeWidth="5"            
                />
                <Line
                  x={550}
                  y={200}
                  points={[0, 0, 0, 100]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />

                {/* Diagonais */}
                <Line
                  x={250}
                  y={100}
                  points={[0, 0, 100, 100]}
                  stroke="green"
                  draggable
                  strokeWidth="5"            
                />

                <Line
                  x={450}
                  y={200}
                  points={[0, 0, 120, -120]}
                  stroke="red"
                  draggable
                  strokeWidth="5"            
                />

                </Layer>
            </Stage>
          </Row>
        </Container>

      </div>
    </>
  );
}

export default RegisterPage;
