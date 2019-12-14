# Traffic Jammer
## User Stories
O João é um estudante universitário que vive em Ilhavo e estuda em Aveiro. Antes de sair de casa quer saber como está o transito no caminho até o departamento dele, para saber o melhor caminho e ter uma boa noção do tempo que vai demorar.

A Maria trabalha para a Camara Municipal de Esgueira. Precisa de saber as zonas de maior congestionamento nas localidades à volta dela para poder enventualmente aprovar medidas que melhorem a situação e saber quais são as ruas com prioridade maior. Recebendo estatisticas sobre as taxas de acidente também ajuda para formar uma decisao informada.


## Work notes
We will work using an Agile Method, scrum-based, where we will meet every week to talk about what has been done or developped since last meeting. Also to update the backlog and define what will be done in our next sprint.

Our repository will be GitLab, where we can share our documents. We chose GitLab because it implements the good features from GitHub that we are used to, but also allow to do continuous delivery and automated that this process requires.

###  Choosing the Database system
We need someting that's capable of doing more than just key-value search, something that is capable of querrying by the values of the street, like searching the most congestioned, the safest streets, which implies averaging the amount of accidents per year, etc.

We don't need to do exact, atomic transactions, and, in this project, an approximate result is enough to get what we want. Knowing this, mongoDB *seems* to be the most ideal technology.However, due to having less experience in MongoDB, and both Mongo and SQL Server can work for our purpose, we're going to choose SQL server, as we have more experience with it and know more details about querying.

```mermaid
graph LR
Dir((<img src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAYFBMVEX///9h2vtT2Pta2ftS2Pvy/P+47f3N8v76/v/o+f7s+v6g5/zZ9f7h9/7w+//1/P+u6v103vts3PuM4/yY5fyA4Pyp6f3E8P2f5/y27P3K8f2/7v2Q5PyG4fxo3PvU9P7IrV7+AAAQVklEQVR4nO1d6bqqvA5etDgCCixwXML93+URtWk60RQRv7Mf3j97L8XSIU3STP35mTFjxowZM2bMmDFjxowZM2bMmDHj/wWLy+FWlE1Z/+Wr3dut7Vb5X31vrbgdLosRevc+jgVjnEd3cM4Za5L0jcbSpOlaezXHWHEcrZ9DceXs0R2J+wfJZlBbm8TW2HXkHodhW7DIAh7XbXBbbR1zW2Os2H6g50Ss7H16zH25Cmuq1JcPzVdYUyPiGDv69Jp7+oZM7bQgEH9pN656B9iN8Uajr+2td3zdEL+yihs8QP6E1jHOckJDuUGfZmvxMN71Hhq0WPx2WF7PyS1i2ihZk3mayRp1Ae8yIrol5+vycOPom2aSMSk4wFBYeYFPt1edI8aH/mZUUr9z4ask7UsJY+T9zXwAO+Yawi6PlFXhpXs3bktlOliUazqRnAD2vrYUhkp0jVn43FGhPB67hPZVWW/W2JoSLfFq1P57sRAvZmfr98dI6fuf9aE/ZR4iu0g4w5umVVLz1wB47XwCc0hemjS2wxTaw3Vr8SoKXx4PsAnde2xXoyXiXBf/Kea6rHbvsi1sxZH6TkLGKJvjggcRL5XvloiHct6rs4gtz3yCZ0wIImX9gniPlzE+oW9OaICs3ve2shHTOSWZFq/OFb4Hl2iI7AYfYzXNwauGvG08rMWsejv3kyGmyov18+cF+izy0x5QzPrtnlORMvrOWCNK5U1Hj/tGDpDVhF6LXc/esR6E4SomlfT0AQ0x2v3s0Koymi4mSGa6437CX1RHe/yIh9jiARLPfS+q5snwLgfi9nrjyf/oAxkWffK/nMr+T6/33fyPjoTy1cOl/9EntpFpouAR2f6yfP26HNbdARA7/+J/9IV1aZxySzpnvIgXDunsIMQDeFuhDpG6hx8QvDsO7ehQiIOFR6PRcMNDDNtSQquZ7HixFS8MM2T+ITlvP06N/MLhEFMah01pgdYwTAFbiG0xlT0KiKZfY9agbMSgbfizH7Qt3sCgbXHTOE3IRhy28d8AUGmAcajSjb4swO6ym5pKB2z83LRqk6zFg1/4HhYBR4snLvLAK4k1JisM2dTSYh16mslggLxcyLNTTJ0hOK1NdkAU24LoL9kjJrP/2SN2Q2TGq6l1GmFpo57XpE762Ehb2JOcqEqL8+h01raX7CaahqQu8yLrVA7xl9SCMGNMZ6j5fZ3XSAwfjNbS0Sldq34zVIeXPZE4H2NAnPGdBm+EVI5GmiykYSOmcKt68jP+WRja/Y8ugESVFfiVHxMkgHgd+cT9NlZ07g3aqMZVgPsQNFSQTtP5ujOyyK/kWqmSQUoQ/26mv240rKlmjIvcb3rvpBZAbmVCi7Dw4ftcz9JRzEzReZVfejR44VCf0pd/o5n35Ca0nen/qFuR+LZRkZOUjMQzBDj0e8SAeGpK3xMw0z76aqXqku02WZq2bbvqcP83TbPNThqKWV8Y3G56Vir9su6X7jdpJMHsQE+kG6cWDnr3pBF8wldisJpFejlXdaP134/uB01dnS+poQEIRjOdPbjDzdTbNqu8KqIYAmAH4BGCG0dFla+QvaL+AqORrOZxYluny6qMmR7xNRyPgZbVMn0IwNeOmDgWQxyA+PFYlSOOTR9nWR2Pgkin8492EFpNNJwkqcOE4KsJNZoORW+/PoEJ4xTuNHpo/D16gD+YhwAXUD8ittUcJqLTtjIi6t0DvB3y66XtxPtiv18LOluv9/tFpwS0l2t+qMmtMV6FR8gHIj31De+5Ok0tp53UqCSIhyDtW9X7208fXMkuctQZUM/vgqxOru0WHeCJB7oM2NbvXV1qr0l9F6vOYXIzCnUktDfH8LrBldU1FWrXCjpMjeuFeGPQAvfptROxjmFydhudWtdL5/I11VVZqjU8Rz/PAZ1yRSRk18rB0u4LuRxTeqwP3KllGga3UyCNdgALqhHA4mZDjOdjjXF9sCyfZDjaCQqsE+Romw4wLZq1A6wENgbH2WGUMZrpEBGPi3wDiptqoJCu3qC3OA7LEF+WZnlh5iDREjr6cTFifTgrllvUKZVMwfrSe6g1AexJtehACHT3x25ZmMknET2ox4Ztre0/zppcHEQhdhed6IDNBFvgQcRgZiM8lWBx3OaNPkhWv3EyPmt0wVmFtklrIVPJZoKiGH5kNIKyf4FIEUFklTZGHpOcHxYs1ISy+/JpDFq8SG6dDdBa+Etl2oE8/Qr9XnUfrJfaQrJikHO4VVq57z5jYwGZApkAbx8SY1eKV8HG3upEKjtXaL0boAHkSmpaXFuEG3BTwdAkuxiiO4JQBM0Gwp8tzWVqglUczFSVfBZW2IW3+F4oL0IBcbGZzSVPqiS/OIJGgNno7dkFT6bsIkdejhNYleCNy2aYqHMMgfnWmIlNEr1OiIxF1lxomWr0dKMBjbgMxqsGd5PizbQNsE+oqoklUlJYNO7tTds4tvzSXJUYhFQSrI6EDBFFaPVnUgvm8LChyIzE/p70zBx82c0R2IL62BbOJqfbGxP5I08wPTiD7yJxL1iTJT5dVxyez5lzDjHv8V4KQ4/rF6UCMKIbXDr9zHwsDXs0zZVTUpgh0K/mzUBokBgVIhCP8oByxGhx2Qs5wMZ7lhbsL84gxcyMPSjsA7T5pCCugW3FIcWv/+0kwyHFhcEmpMSag+ZWiSU093vlGqBNlIOqDQ0ShLkkEspWBJ8YLWAJ+goHPF0OrGx7EOZcF0SQA897+JYJGCJhPkp4O0l3zrUFMr29PeOz9f9Pb5CkrMhgOe+6wBISbRB7bYUMJ9+1bwktDv6tVqmBeEgBe513EQXrINvJ1Dk3N1YZ9cOYc3XbkqP6hTT2MSaQsmQbRKbMucHLsv4ltNDKQvkFOQYVdoPHgwO8kR5ghX00pgap71MD5j5L8E/o/pgljfcOSNe8oDk3N43XKWFKF7y1Q1KraOnCIq4yRE/vW0IfJ+1g/AYvYkA/hDe8fyOK2NiQOhtn6JAlicZXw8YW2ryXYeEhxhDBa/oJW2QWhuSjylOTuYS6MLHAIg5kqFGIxVdo6v0S8d8foci4DaHSfGwqXUgqDbG+0Kj0TU5juiq8A7Qwk9MnOQ1IC7pB94iZu7GIN6+0ME4DWORTs71/5IbwrPsAiY/VMnMRB0h8vIQBhleixA/X2lKFlxjBiplvIxpq2U5tkGx5hV94uJNQpMmR/78f1rypHh7Bf72qujQ80yZv8fHTE80lEdBvGbhLato4ARtz7llD/fFfvUGSwJBpHX5VXVoxGoq4lT0Ri6hbMdpeK4bOFqQVwzkHFqzBFkVx0QyzRJ1Gt0SdaLzxMcAgSxRStAiVK6Q1cQfWRKNHAdbEFlrZgTXR22lUdYMmx5FxzDd/wGcKJMZMEeYYoiWEHyzCJ8kRfLwGbQNqsDuyk3uqHoqDU8cRYe0teoi1fCczFwf0o24tBBf2HKFQ5UViQZ8fhZ+xoi9DnOyZOVs8M5aOw5eKZ6YvtmqDPTMB0RFIm+Q9y6iVbevzru1+Ne/ar8VjAHP09NsTvGsH5AgOC3XHZOUOWdE8pCDcraUItgfkIT3YeBgwq5ca4PWQKsE+FqLvhVIDwVUS2OWVds3mdnVOkuS8crDom7M96+Nq8eGQGg1PKJEKUVxbxtjq5xXgaqbEIAAkBXDwvEckprXawQHhXy1XN05hcOKeaJMhiXSwYoRok5UWbcIHxZvuNc8ta86qPBXqB4oYgmV4I2II6X1CkKpkuj9rtYd9lRfdWOrxVewPEavQDLDZCmxIgdV5kHEG8xWI+kL0k/4ZvXojA3p3084yXZC1mGIgUjyBQQoixk2VFE/sdTLdmKHm8e29qO9VpKsjnJXnDRqMqmpLrSSw6rxdI1KiLzdnszQ9i97PSlya4eScNYfMFpr4gzNjg94Cv3JE0LbZwYi77DjMKCn6a0uUMI6CVnecPOCFCCg4YWnHS1Dt7VHQo0V63wUTPZIdmE1A+J6MZNfVl95I9rfHhXG10MgTzd8rT1BAfkNuXeYc4E/X6fLPmY1Qjl/qM/11Z5Swplq2glpXNr7fCyljBNtYtMuqceY13vX2z6QGLSy8DA8zqk/LdrOWrv3grKC/n/WmXZ7qqCdps+PlH6wXlSXu1KfoldkVSb93aGZXEXkzu6Lk49Ux0t5Bah2qk3x5XMn0vBdEct7quMyTgOy86K2LiAKQ5Y5YPLNTkE8ZoxRL+JvZ7v1wNVXmU5Ys/9ezZJENhZEpdhg4VC6YONNZqGzscjkV7xQZ6Bnb486u0wWq03w8QVaBWnEgu96HGY82zm5s8X1w1+yLFQcsVSO27bnycnv/0DppU51bZMr5TtUIZ+WPfbY6J7eCx8GVP2Je3JLzKjOO61+p/OGv3rLeZnhxrMVb8FJnWycj+Ur1FqjA06c+oeKB2X67yZ41eNpn/Z1ss92jCjx9ghyKiU5ZgQeM0/1PwRDt8QbgAPf4G8Q8TXnl0yiVsGRO5X+wEhaxmpl08lvMYfL6Ep/77AvVzMgV6aQr0sjCQBUjffvrCxXpoMyftzazTDDSAh9kaIE/lecLVQX//cqQAdU9UQVIzCikg5JSS1i8bmhGczgGVmiV5Ji496cN01doFeybZBFFPFOYx659PNaCanJxMbhS8vMAhMoN0vJFpq+ULPpHNFnKYJMH893IARK7PH2169CK5RHgLjMWSOH+r1YsD646L6+d5c0WVZ2nXnUwedV5uDKELIHR1cEoGoks3oTID3a7DsWAyxiW5nk4wHP7vXtmApyvJ32ILKAE0eQ3eAy6hUWLjA2qX/O1W1j+/Zt0/t3bkAZufESngTWWvnfPTNCUKi6msEIkk99KNuRmufX/1c1yA24H3FtuB6TzqelvBxRZiuQT6Zs3PIoT93Q3PIbe0olzo/B/qVQ+/S2dgTetosQgHqX4ptWw49eEZ/yw23JRQR/e3E9P+DpgWp/t8WWfRIh5T7nx+JGFgwvyhN14PP0dJQQzBr4kHqga31rtK2P085Vbq6GL3o2I78xjUpH5xR97p0mYhaaMVYBZ7acbpfKi4mA64C88VQ8zOsWMB8i66rWVXbEPNFbZxBUFH/N+nipsdfQyJ2MA+u2W2krtU3O74Q3aW4NUJpWO1HcaBJm6NWil+DAvTBVtjzVV7naSQiD0tLEYMlHN/t6rEo/hyGdR8nK4Q9oBrwqu+fomIGzZtoeuSvg7d5YNOCrBCiyyNQWRmcFZP28CuXc1+tpqxb9Z4TZY7dQyt4zrGV+S5053NhSQko43RxDFm7Nek9oj7rRLZnlcnOFcvT6iYnrT7sIHsO7F6+S8zLvYXi0eipU+Fp+V2hh5F2ucL89JzbG+N8mYVGxVPmGLFLXmiRqw5JcarU1moVHQekpe8PiXtncWv2a1dRWDsv1GwKV3iK7iwzaoyZLmAN+ru/4GWnfofmwWx+5vylI1X7Q1cWSpgp197nl8C484T2/2MfZJmylwNAL3uSOP2Y8uF9psjF5l6FO41CJo9hHbW751Z1F6KGPUGqu/tgMVrFf5X12URV2d2/eVx317rh6t/eWria/pmjFjxowZM2bMmDFjxowZM2bMmDFjxowZM2bM+Cj+B5V7rnS0Np+RAAAAAElFTkSuQmCC' width='40' />))
A[Rua]; B[Sentido]; C[Acidente]; D[Congestao]
A -- Connects --> A;
A -- Has --> B
B -- Happen --> C
B -- Has --> D
```

 - Rua is a table with the attributes: 
     - Name of street, 
     - beginning coordinates, 
     - ending coordinates, 
     - length, 
     - autogenerated long ID number for primary key;
 - Sentido is a weak entity:
     - Boolean value for increasing (1) vs decreasing(0)
     - ID of street
     - Number of cars
     - Int value for accident 
     - Prime key: id+bool
 - Acidente is basically a logger entity:
     - 
Messaging queue may be done with RabbitMQ since we already have some knowledge using it from previous classes.

Backend will be done in Django, since one of our programmers can never seem to get Maven right, and as Django is done in Python, which is a languange the whole development team is already very familiar with, and is simpler and more straightforward in terms of handling HTTP requests.

Front end development may be done with ReactJS, depending on how Tomas feels about it lmao. (easier if we also want the app, as we only need to develop once)

Interface has to be seen afterwards with Tomas, but with the information at the moment we can either just try to get the most out of the Google API, or just do a simple interface from scratch that takes a very minimalistic graph or a simple grid. (Either way we will need to manually integrate and create streets)

## What the client wants?
Traffic point of the user: como está o transito à volta dele?
Street statistics: estatisticas de acidente, trafico medio, que rua se conecta a qual, comprimento da rua, inicio e 
Extra: Route dum sitio (if able)

## Street attributes

## Roles
Team Manager - Tomas 
Product Owner - Mota
Architect - Joao
DevOps master - Pedro

### Notes
We are the group 35
det-engsoft-14.ua.pt
Use
