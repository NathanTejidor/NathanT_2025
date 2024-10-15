
  let data = JSON.parse(jsonData);
  
  
  console.log(data.users[0].name); // Output: Alice
  

  data.users[1].active = true;
  
  
  data.users[0].age = 30;
  
  
  data.users[1].tags.push("artist");
  

  const newUser = {
      id: 3,
      name: "Charlie",
      email: "charlie@example.com",
      active: true,
      tags: ["new", "friend"]
  };
  data.users.push(newUser);
  

  const updatedJsonData = JSON.stringify(data, null, 2);
  console.log(updatedJsonData);
  