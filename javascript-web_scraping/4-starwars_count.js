#!/usr/bin/node

const request = require('request');

const options = {
  url: process.argv[2]
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const r = /18/;
    const movies = data.results;
    let i = 0;
    let count = 0;
    for (i = 0; i < movies.length; i++) {
      for (const cindx in movies[i].characters) {
        if (movies[i].characters[cindx].match(r)) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
}

request(options, callback);
