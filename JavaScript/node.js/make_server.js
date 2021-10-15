var http = require('http');
var fs = require('fs');
const hostname = "127.0.0.1";
const port = 8000;

http.createServer(function(req, res){
    fs.readFile('index.html',function (err, data){
        res.writeHead(200, {'Content-Type': 'text/html','Content-Length':data.length});
        res.write(data);
        res.end();
    });
}).listen(8000);
console.log("Server is running on http://" + hostname + ":" + port)
