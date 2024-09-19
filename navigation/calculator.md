---
layout: post
title: Calculator 
permalink: /calculator/
description: Calc, short for calculator btw if you didn't know
toc: true
comments: false
---

 <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Simple JavaScript Calculator</title>
       <link rel="stylesheet" href="styles.css">
   </head>
   <body>
       <div class="calculator">
           <h1>Calculator</h1>
           <select id="operation">
               <option value="add">Addition</option>
               <option value="subtract">Subtraction</option>
               <option value="multiply">Multiplication</option>
               <option value="divide">Division</option>
               <option value="percentage">Percentage Change</option>
           </select>
           <input type="number" id="num1" placeholder="Enter first number">
           <input type="number" id="num2" placeholder="Enter second number">
           <button onclick="calculate()">Calculate</button>
           <p id="result"></p>
       </div>
       <script src="script.js"></script>
   </body>
   