function loginUser(event) {
  event.preventDefault();

  let email = document.getElementById("email").value;
  let password = document.getElementById("password").value;
  let message = document.getElementById("message");

  if (email === "" || password === "") {
    message.style.color = "red";
    message.innerHTML = "Please fill all fields";
  } 
  else if (email === "admin@gmail.com" && password === "12345") {
    message.style.color = "green";
    message.innerHTML = "Login successful!";
  } 
  else {
    message.style.color = "red";
    message.innerHTML = "Invalid email or password";
  }
}

function togglePassword() {
  let password = document.getElementById("password");
  let toggleText = document.querySelector(".password-box span");

  if (password.type === "password") {
    password.type = "text";
    toggleText.innerHTML = "Hide";
  } else {
    password.type = "password";
    toggleText.innerHTML = "Show";
  }
}