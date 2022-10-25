
const config = {
    // 一些系统配置
    "baseURL":'http://localhost:8000',
    "ExpireTime" :new Date(new Date().getTime() + 15 * 60 * 1000),// cookie 15分钟后过期
}

export default config