## Code Execution in verbose=False:

Ask: tell me the occupation of Ali?  

Answer: Based on the information I retrieved, **Ali's occupation is Backend Developer**. He is a 21-year-old male who works as a Backend Developer.
Ask: what is the contact no of Usman?

Answer: Based on the information retrieved, **Usman's contact number is 0337-9117448**. He is a 22-year-old male who works as an ML Developer and has knowledge of IoT.
Ask: who is female in all developers?

Answer: Based on the data of all developers, **Sana is the only female developer** in the list. She is a 23-year-old Frontend Developer who is a master in HTML, CSS, JS, and React.
Ask: how many developers are in total?

Answer: Based on the data retrieved, there are **4 developers in total**:

1. **Ali** - 21 years old, Male, Backend Developer
2. **Usman** - 22 years old, Male, ML Developer (with IoT knowledge)
3. **Sana** - 23 years old, Female, Frontend Developer
4. **Anas** - 24 years old, Male, Blockchain Developer

So the total count is 4 developers.


## Code Execution in verbose=True:

Ask: tell me the occupation of Ali?   


> Entering new AgentExecutor chain...

Invoking: `get_person_details` with `{'name': 'Ali'}`
responded: I'll help you find Ali's occupation. Let me get the details for Ali.

Details are {
  "name": "Ali",
  "age": 21,
  "gender": "male",
  "profession": "Backend Developer",
  "about": "His full name is Ali Raza Riaz Ahmad Warsi Rajpoot.",
  "contact": "0319-0478213"
}Based on the information retrieved, **Ali's occupation is Backend Developer**. He is a 21-year-old male who works as a Backend Developer.

> Finished chain.

Answer: Based on the information retrieved, **Ali's occupation is Backend Developer**. He is a 21-year-old male who works as a Backend Developer.
Ask: what is the contact no of Usman?


> Entering new AgentExecutor chain...

Invoking: `get_person_details` with `{'name': 'Usman'}`
responded: I'll help you find Usman's contact number. Let me search for his details.

Details are {
  "name": "Usman",
  "age": 22,
  "gender": "male",
  "profession": "ML Developer",
  "about": "Usman is an intelligent Developer and is hardworking. He also has a great knowlegde of IOT.",
  "contact": "0337-9117448"
}Based on the information retrieved, **Usman's contact number is 0337-9117448**. He is a 22-year-old male who works as an ML Developer and has knowledge of IoT.

> Finished chain.

Answer: Based on the information retrieved, **Usman's contact number is 0337-9117448**. He is a 22-year-old male who works as an ML Developer and has knowledge of IoT.
Ask: who is female in all developers?


> Entering new AgentExecutor chain...

Invoking: `get_all_people` with `{}`
responded: I'll get the details of all people in the database to identify which developers are female.

[
  {
    "name": "Anas",
    "age": 20,
    "gender": "male",
    "profession": "Blockchain Developer",
    "about": "Anas is  a Blockchain developer since 2024 and has a strong grip in his profession.",
    "contact": "0310-4573829"
  },
  {
    "name": "Ali",
    "age": 21,
    "gender": "male",
    "profession": "Backend Developer",
    "about": "His full name is Ali Raza Riaz Ahmad Warsi Rajpoot.",
    "contact": "0319-0478213"
  },
  {
    "name": "Usman",
    "age": 22,
    "gender": "male",
    "profession": "ML Developer",
    "about": "Usman is an intelligent Developer and is hardworking. He also has a great knowlegde of IOT.",
    "contact": "0337-9117448"
  },
  {
    "name": "Sana",
    "age": 23,
    "gender": "female",
    "profession": "Frontend Developer",
    "about": "Sana is professional frontend developer. She is master in HTML, CSS, JS, REACT.",
    "contact": "0302-6206029"
  }
]Based on the data from all developers, **Sana is the only female developer** in the database. Here are her details:

- **Name:** Sana
- **Age:** 23
- **Gender:** Female
- **Profession:** Frontend Developer
- **About:** Sana is a professional frontend developer. She is a master in HTML, CSS, JS, REACT.
- **Contact:** 0302-6206029

All the other developers (Anas, Ali, and Usman) are male.

> Finished chain.

Answer: Based on the data from all developers, **Sana is the only female developer** in the database. Here are her details:

- **Name:** Sana
- **Age:** 23
- **Gender:** Female
- **Profession:** Frontend Developer
- **About:** Sana is a professional frontend developer. She is a master in HTML, CSS, JS, REACT.
- **Contact:** 0302-6206029

All the other developers (Anas, Ali, and Usman) are male.
Ask: how many developers are in total?


> Entering new AgentExecutor chain...
Based on the data retrieved, there are **4 developers in total** in the database. Here's the complete list:

1. **Anas** - 20 years old, Male, Frontend Developer
2. **Ali** - 21 years old, Male, Backend Developer  
3. **Usman** - 22 years old, Male, ML Developer
4. **Sana** - 23 years old, Female, Frontend Developer

So the total count is 4 developers.

> Finished chain.

Answer: Based on the data retrieved, there are **4 developers in total** in the database. Here's the complete list:

1. **Anas** - 20 years old, Male, Frontend Developer
2. **Ali** - 21 years old, Male, Backend Developer
3. **Usman** - 22 years old, Male, ML Developer
4. **Sana** - 23 years old, Female, Frontend Developer

So the total count is 4 developers.
