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
import { Stage, Layer, Star, Text } from 'react-konva';
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
y        style={{
          backgroundImage: "url(" + require("assets/img/grid_neon2.png") + ")",
        }}
      >
        <div className="" />
        <Container>
          <Row>
            <Col style={{backgroundColor:'white'}} className="ml-auto mr-auto" lg="4" >
            <Stage width={window.innerWidth} height={window.innerHeight}>
                <Layer>
                <Text text="Try to drag a star" />
                {[...Array(10)].map((_, i) => (
                    <Star
                    key={i}
                    x={Math.random() * window.innerWidth}
                    y={Math.random() * window.innerHeight}
                    numPoints={5}
                    innerRadius={20}
                    outerRadius={40}
                    fill="#89b717"
                    opacity={0.8}
                    draggable
                    rotation={Math.random() * 180}
                    shadowColor="black"
                    shadowBlur={10}
                    shadowOpacity={0.6}
                    />
                ))}
                </Layer>
            </Stage>
            </Col>
          </Row>
        </Container>

      </div>
    </>
  );
}

export default RegisterPage;
