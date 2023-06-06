// Function to perform arithmetic operations asynchronously
function performOperation( a, b) {
    return new Promise((resolve, reject) => {

        setTimeout(()=>{
            let arr = [a+b , '+']
            console.log(`The result of ${a} ${arr[1]} ${b} is ${arr[0]}`);
            resolve(arr);
        },1000);

        setTimeout(()=>{
            let arr = [a-b , '-']
            console.log(`The result of ${a} ${arr[1]} ${b} is ${arr[0]}`);
            resolve(arr);
            
        },2000);

        setTimeout(()=>{
            let arr = [a*b , '*']
            console.log(`The result of ${a} ${arr[1]} ${b} is ${arr[0]}`);
            resolve(arr);
        },3000);

        setTimeout(()=>{
            if(b!==0)
            {
                arr = [a/b , '/']
                console.log(`The result of ${a} ${arr[1]} ${b} is ${arr[0]}`);
                resolve(arr);
            }
            else reject("Zero divsion error");
        },4000);
     });
  }
  
  // Function to display the result synchronously using await
  async function displayResult( a, b) {
    try {
          await performOperation(a, b);
    } 
    catch (error) {
      console.log('Error:', error);
    }
  }
  
  // Call
  displayResult( 5, 3);
  
  