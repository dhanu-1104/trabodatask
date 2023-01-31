 function validateform(){
    // Get the values of the input fields
    var username = document.login.username.value;
    var password = document.login.password.value;
   
    // Check if the entered username and password match
    if (username === "traboda" && password === "amrita") {
  
      // Redirect the user to the login-success.html page
      window.location.href = "login-success.html";
    } else {
      alert("Incorrect username or password");
    }
    return false;
  }
  