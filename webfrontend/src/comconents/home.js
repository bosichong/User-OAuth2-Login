import img_01 from '../img_01.jpeg'
import axios from 'axios';
import { useState, useEffect } from 'react';
import cookie from 'react-cookies'
import { useNavigate } from "react-router-dom"
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';

import config from '../config'

export default function Home() {
  // cookie.remove("access_token")
  const token = cookie.load("access_token")
  const navigate = useNavigate();
  const baseURL = 'http://localhost:8000'


  useEffect(() => {
    // console.log(token)
    // 如果没有token的话就跳转到login页面
    if (token == undefined) {
      navigate("/login")
    }
  }, [])

  function handleSubmit(e){
    cookie.remove("access_token")
    cookie.remove("username")
    cookie.remove("email")
    navigate("/login")

  }
  return (
    <Container component="main" >
      <Card sx={{ mx: "auto", my: 10, maxWidth: 550 }}>
        <CardMedia
          component="img"
          height="140"
          image={img_01}
          alt="green iguana"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {cookie.load("username")}
          </Typography>
          <Typography variant="body2" color="text.secondary">
          {cookie.load("email")}
          </Typography>
        </CardContent>
        <CardActions>
          <Button size="small" onClick={handleSubmit} >退出登陆</Button>
        </CardActions>
      </Card>
    </Container>
  );
}
