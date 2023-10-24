#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let def = {};
request(url, function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    const abc = JSON.parse(body);
    abc.characters.forEach(function (item, index, array) {
      request(item, function (err, r, content) {
        if (err) {
          console.log(err);
        } else {
          def = JSON.parse(content);
          console.log(def.name);
        }
      });
    });
  }
});
