function add(a, b)
 {
    return new Promise((resolve) => 
    {
      setTimeout(() =>
     {
        resolve(a + b);
      }, 10);
    });
  }
  
  function subtract(a, b) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(a - b);
      }, 1500);
    });
  }
  
  function multiply(a, b) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(a * b);
      }, 1200);
    });
  }
  
  function divide(a, b) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (b === 0) {
          reject("Division by zero is not allowed.");
        } else {
          resolve(a / b);
        }
      }, 2000);
    });
  }
  
  const num1 = parseFloat(prompt("Enter the first number:"));
  const num2 = parseFloat(prompt("Enter the second number:"));
  
  async function performOperations() {
    try {
      const additionResult = await add(num1, num2);
      console.log("Addition result:"+additionResult);
  
      const subtractionResult = await subtract(num1, num2);
      console.log("Subtraction result:", subtractionResult);
  
      const multiplicationResult = await multiply(num1, num2);
      console.log("Multiplication result:", multiplicationResult);
  
      const divisionResult = await divide(num1, num2);
      console.log("Division result:", divisionResult);
    } catch (error) {
      console.log("Error:", error);
    }
  }
  
  performOperations();
