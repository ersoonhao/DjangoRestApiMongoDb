import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:8080/api",
  headers: {
    "Content-type": "application/json"
  }
});


// export default axios.create({
//     baseURL: "http://django-app.eba-ycxqwbvu.ap-southeast-1.elasticbeanstalk.com:8080/api",
//     headers: {
//       "Content-type": "application/json"
//     }
//   });