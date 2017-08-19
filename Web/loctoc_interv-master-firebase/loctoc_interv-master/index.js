var express = require('express');
var app = express();
var path = require('path');

var http = require('http').Server(app);

//app.set('port', (process.env.PORT || 5000));

//app.use(express.static(path.join(__dirname, 'client')));
//
//
//// views is directory for all template files
////app.set('views', __dirname + '/views');
////app.set('view engine', 'ejs');
//
//app.get('/', function(request, response) {
//  response.render('app.html');
//});

app.use(express.static('client'));

app.get('/', function (req, res) {

    res.sendfile('client/app.html');

});

//app.listen(app.get('port'), function() {
//  console.log('Node app is running on port', app.get('port'));
//});




var server = http.listen(process.env.PORT || 3000, function () {
    var host = server.address().address;
    var port = server.address().port;

    console.log('App listening at http://%s:%s', host, port);
});
