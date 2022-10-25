import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
import cookie from 'react-cookies'
import { useNavigate } from "react-router-dom"

import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';

import config from '../config'






const theme = createTheme();

function Login() {

    const [username, setNasename] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate()
    const baseURL = config.baseURL

    function handleSubmit(event) {
        event.preventDefault()// 阻止表单提交
        // 获取token
        axios.post(baseURL + '/v1/token', {
            username: username,
            password: password,
        },
            { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } },
        ).then(function (response) {
            cookie.save("access_token", response.data.access_token, { expires: config.ExpireTime })
            cookie.save("token_type", response.data.token_type, { expires: config.ExpireTime })
            getUser()
            
        }).catch(function (error){
            console.log(error.response.data.detail)
            alert(error.response.data.detail)
        })

        function getUser() {
            // 通过接口获取用户资料,并保存到cookie
            axios.get(baseURL + "/v1/users/me", {
                headers: {
                    "accept": "application / json",
                    "Authorization": "Bearer " + cookie.load("access_token")
                }
            }).then((function (response) {
                let user = response.data
                cookie.save("username", user.username, { expires: config.ExpireTime })
                cookie.save("email", user.email, { expires: config.ExpireTime })
                navigate("/home")
            }))
        }

    }

    function handleChangeUsername(e) {
        setNasename(e.target.value)
    }

    function handleChangePassword(e) {
        setPassword(e.target.value)
    }

    return (

        <Container component="main" maxWidth="xs">
            <CssBaseline />
            <Box
                sx={{
                    marginTop: 8,
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                }}
            >
                <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5">
                    Sign in
                </Typography>
                <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        id="username"
                        label="UserName"
                        name="username"
                        autoComplete="username"
                        autoFocus
                        onChange={handleChangeUsername}
                        value={username}
                    />
                    <TextField
                        margin="normal"
                        required
                        fullWidth
                        name="password"
                        label="Password"
                        type="password"
                        id="password"
                        autoComplete="current-password"
                        onChange={handleChangePassword}
                        value={password}
                    />
                    {/* <FormControlLabel
                        control={<Checkbox value="remember" color="primary" />}
                        label="Remember me"
                    /> */}
                    <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}
                    >
                        Sign In
                    </Button>
                    <Grid container>
                        <Grid item xs>
                            <Link href="#" variant="body2">
                                Forgot password?
                            </Link>
                        </Grid>
                        <Grid item>
                            <Link href="#" variant="body2">
                                {"Don't have an account? Sign Up"}
                            </Link>
                        </Grid>
                    </Grid>
                </Box>
            </Box>
        </Container>
    );
}





// import { useState, useEffect } from 'react';
// import Box from '@mui/material/Box';
// import TextField from '@mui/material/TextField';
// import Button from '@mui/material/Button';
// import axios from 'axios';




// function Login() {
//     const [username,setNasename] = useState("")
//     const [password,setPassword] = useState("")

//     function handleSubmit(event){
//         event.preventDefault()// 阻止表单提交
//         console.log("提交表单!")
//         axios.get(baseURL+'/test/').then(function (response){
//             console.log(response)
//             // todo 继续登陆接口测试
//         })

//     }
//     return (
//         <form onSubmit={handleSubmit}>
//             <Box
//                 sx={{
//                     mx: "auto", my: 10, maxWidth: 345 ,
//                     '& .MuiTextField-root': { m: 1, width: '25ch' },
//                 }}
//                 noValidate
//                 autoComplete="off"
//             >
//                 {/* <div><input type="text" value={this.state.username} onChange={this.handleChange} /></div> */}
//                 <div><TextField name="username" type="text" defaultValue={username}  id="outlined-basic" label="username" variant="outlined" /></div>
//                 <div><TextField name="password" type="password" defaultValue={password} id="outlined-basic" label="password" variant="outlined" /></div>
//                 <div><Button type="submit" value="提交" variant="contained" color="primary">提交</Button></div>
//             </Box>
//         </form >
//     )
// }

export default Login

