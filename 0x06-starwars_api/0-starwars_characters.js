#!/Users/serahnderi/.nvm/versions/node/v10.24.1/bin/node


const request = require('request');
const argv = require('process').argv;

request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (err, res, body) {
    if (err) throw err;
    const actors = JSON.parse(body).characters;
    extractOrder(actors, 0);
});

const extractOrder = (actors, x) => {
    if(x === actors.length) return;
    request(actors[x], function (err, res, body) {
        if (err) throw err;
        console.log(JSON.parse(body).name);
        extractOrder(actors, x + 1);
    });
};