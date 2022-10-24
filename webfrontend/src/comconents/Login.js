import React from 'react';
import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import axios from 'axios';

const baseURL = 'http://localhost:8000'


function Login() {
    const [username,setNasename] = useState("")
    const [password,setPassword] = useState("")

    function handleSubmit(event){
        event.preventDefault()// 阻止表单提交
        console.log("提交表单!")
        axios.get(baseURL+'/test/').then(function (response){
            console.log(response)
            // todo 继续登陆接口测试
        })

    }
    return (
        <form onSubmit={handleSubmit}>
            <Box
                sx={{
                    mx: "auto", my: 10, maxWidth: 345 ,
                    '& .MuiTextField-root': { m: 1, width: '25ch' },
                }}
                noValidate
                autoComplete="off"
            >
                {/* <div><input type="text" value={this.state.username} onChange={this.handleChange} /></div> */}
                <div><TextField name="username" type="text" defaultValue={username}  id="outlined-basic" label="username" variant="outlined" /></div>
                <div><TextField name="password" type="password" defaultValue={password} id="outlined-basic" label="password" variant="outlined" /></div>
                <div><Button type="submit" value="提交" variant="contained" color="primary">提交</Button></div>
            </Box>
        </form >
    )
}

export default Login

