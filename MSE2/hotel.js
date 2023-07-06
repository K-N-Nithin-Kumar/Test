function bookflight()
{
    return new Promise((resolve,reject)=>
    {
        setTimeout(()=>
        {
            const flightbooked = false;
            if(flightbooked)
            {
                console.log("Flight is booked");
                resolve();
            }
            else{
                reject("Flight booking failed");
            }
        },1000)
    });
}
function bookHotel()
{
    return new Promise((resolve,reject)=>
    {
        setTimeout(()=>
        {
            const hotelbooked = true;
            if(hotelbooked)
            {
                console.log("Hotel is booked");
                resolve();
            }
            else{
                reject("Hotel booking failed");
            }
        },2000);
    }
    )
}
bookflight().then(
    ()=>
    {
        return bookHotel();
    }
).then(
    ()=>
    {
        console.log("Everything booked successfully");
    }
).catch(
    ()=>
    {
        console.log("Error occured while booking");
    }
)
