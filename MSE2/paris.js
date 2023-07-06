let location = "pris";
const fun = (locatio)=>new Promise((resolve,reject)=>{
      if(locatio==="paris")
      {
        resolve("Plan ok")
      }
      else{
        reject("Not ok");
      }
});

fun(location).then(res=>{
    console.log(res);
}).catch(res=>{
    console.log(res);
})
