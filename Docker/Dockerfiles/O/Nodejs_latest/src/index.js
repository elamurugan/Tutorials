//Dependecy : Nodejs_latest
const express = require('express');
const app = express();
const host = "127.0.0.1";
const port = 8888;

app.get('/', (req, res) => res.send('Hello World from Node.js Docker Application!'));

// var server = app.listen(port,host, () => console.log(`Example app listening on port ${port}!`))

var server = app.listen(port,host, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log('Example Nodejs app listening at http://%s:%s', host, port);
});
