function bookFlight() {
    return new Promise((resolve, reject) => {
      // Simulating flight booking with a delay of 2 seconds
      setTimeout(() => {
        console.log('Flight booked successfully');
        resolve();
      }, 2000);
    });
  }
  
  function bookHotel() {
    return new Promise((resolve, reject) => {
      // Simulating hotel booking with a delay of 2 seconds
      setTimeout(() => {
        console.log('Hotel booked successfully');
        resolve();
      }, 2000);
    });
  }
  
  function bookFlightAndHotel() 
  {
    bookFlight().then(() =>
     {
        return bookHotel();
      }).then(() => 
      {
        console.log('Booking completed successfully');
      }).catch((error) => 
      {
        console.log('Error while booking:', error);
      });
  }
  
  // Calling the function to book flight and hotel
  bookFlightAndHotel();
