#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, r, body) {
  console.log(err || JSON.parse(body).title);
});
