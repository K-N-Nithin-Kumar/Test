let available = [1,4,6,8,9,14,18,22]
function bookFlight(passenger_time)
{
    return new Promise((resolve,reject)=>{
        let find = available.indexOf(passenger_time)
        if(find>=0){
            resolve("Flight is booked so hotel is booked");
        }
        else{
            reject("Flight is not available so hotel is not booked");
        }
    });
}

function bookHotel(){
    let time = Number(prompt('Enter the time')); 
    const msg = bookFlight(time);
    msg.then((booked)=>{
        alert(booked)
    }); 
    msg.catch(notbooked=>{
        alert(notbooked);
    });
}

bookHotel();