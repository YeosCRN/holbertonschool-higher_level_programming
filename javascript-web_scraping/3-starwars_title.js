#!/usr/bin/node

const request = require('request');

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info.title);
  }
}

request(options, callback);
