#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (err, r, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    printCharacters(chars, 0);
  }
});

function printCharacters(chars, index) {
  request(chars[index], function (err, r, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        printCharacters(chars, index + 1);
      }
    }
  });
}
