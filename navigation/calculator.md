---
layout: post
title: Calculator ➗
permalink: /calculator/
description: Calc, short for calculator btw if you didn't know
toc: true
comments: false
---



<head>
  <style>
    body {
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #000000;
    }

    .calculator {
      border-radius: 10px;
      padding: 20px;
      background-color: #4a4a49 ;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    #display {
      width: 100%;
      height: 50px;
      margin-bottom: 10px;
      text-align: right;
      padding: 10px;
      font-size: 24px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #8fa86d;
    }

    .buttons {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    }

    button {
      padding: 20px;
      font-size: 18px;
      border: none;
      border-radius: 5px;
      background-color: #303030;
      cursor: pointer;
      transition: background-color 0.3s ease;
    }

    button:hover {
      background-color: #545453;
    }

    button:active {
      background-color: #0000;
    }
  </style>
</head>
<body>
  <div class="calculator">
    <input type="text" id="display" disabled>
    <div class="buttons">
      <button onclick="clearDisplay()">C</button>
      <button onclick="deleteLast()">DEL</button>
      <button onclick="appendToDisplay('(')">(</button>
      <button onclick="appendToDisplay(')')">)</button>
      <button onclick="appendToDisplay('7')">7</button>
      <button onclick="appendToDisplay('8')">8</button>
      <button onclick="appendToDisplay('9')">9</button>
      <button onclick="appendToDisplay('/')">/</button>
      <button onclick="appendToDisplay('4')">4</button>
      <button onclick="appendToDisplay('5')">5</button>
      <button onclick="appendToDisplay('6')">6</button>
      <button onclick="appendToDisplay('*')">*</button>
      <button onclick="appendToDisplay('1')">1</button>
      <button onclick="appendToDisplay('2')">2</button>
      <button onclick="appendToDisplay('3')">3</button>
      <button onclick="appendToDisplay('-')">-</button>
      <button onclick="appendToDisplay('0')">0</button>
      <button onclick="appendToDisplay('.')">.</button>
      <button onclick="calculate()">=</button>
      <button onclick="appendToDisplay('+')">+</button>
    </div>
  </div>

  <script>
    function appendToDisplay(value) {
      document.getElementById("display").value += value; // Append the value to display
    }

    function clearDisplay() {
      document.getElementById("display").value = ''; // Clear the display
    }

    function deleteLast() {
      let currentDisplay = document.getElementById("display").value;
      document.getElementById("display").value = currentDisplay.slice(0, -1); // Remove the last character
    }

    function calculate() {
      let expression = document.getElementById("display").value;
      try {
        // Evaluate the expression safely
        let result = eval(expression);
        document.getElementById("display").value = result;
      } catch (error) {
        document.getElementById("display").value = 'Error'; // Show error if eval fails
      }
    }
  </script>
</body>
   