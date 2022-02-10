const express = require('express')
const app = express()
const port = 3000

const mongoose = require('mongoose')
mongoose.connect('mongodb+srv://seo0ojin:abcd1234@boilerplate.tsbwi.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',{
    /*
    몽구스 6.0 버전 이상은 항상 아래 조건으로 기억하고 실행하기 때문에 지원하지 않음
    userNewUrlParser: true, 
    useUnifiedTopology: true, 
    useCreateIndex: true, 
    useFindAndModify: false
    */
}).then(() => console.log('MongoDB Connected...'))
.catch(err => console.log(err));


app.get('/', (req, res) => {
  res.send('Hello World! 안녕하세요')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})