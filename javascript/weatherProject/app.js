const express = require("express");
const https = require("https");
const bodyParser = require("body-parser");
const app = express();


app.use(bodyParser.urlencoded({extended:true}));

app.get("/", function(req, res){
    res.sendFile(__dirname + "/index.html");
    
})

app.post("/", function(req, res){
    const query = req.body.cityName;
    const appID = "a7237168b9c3d0b7ba9b9fa4a7da7d6d" ;
    const unit  = "metric";
    const url = "https://api.openweathermap.org/data/2.5/weather?q="+query+"&appid=" + appID +"&units="+unit
    https.get(url, function(response){
        console.log(response.statusCode);
        response.on("data", function(data){
            const result = JSON.parse(data)
            const temp = result.main.temp
            const desc = result.weather[0].description
            const icon = result.weather[0].icon
            const imageURL = "http://openweathermap.org/img/wn/" + icon +  "@2x.png"
            res.write("<p> weather description is " + desc + "</p>");           
            res.write("<h1>The temprature in " + query + " is " + temp + "celcius </h1>");
            res.write("<img src=" + imageURL + ">")
            res.send();
        })
    })
})


app.listen(3000, function(){
    console.log("Server Started");
})