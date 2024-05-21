#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request.get(url, function (error, response, body) {
  if (error) {
    console.error('Error reading file:', error);
  }
  const todos = JSON.parse(body);
  const completed = {};
  for (const todo of todos) {
    if (todo.completed) {
      if (completed[todo.userId]) {
        completed[todo.userId]++;
      } else {
        completed[todo.userId] = 1;
      }
    }
  }
  console.log(completed);
}
);
