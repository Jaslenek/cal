function onPredictClicked() {
let gender = $("#gender").val();
let age = $("#age").val();
let height = $("#height").val();
let weight = $("#weight").val();
let duration = $("#duration").val();
let heart_rate = $("#heart_rate").val();
let body_temp = $("#body_temp").val();


$.post("http://127.0.0.1:5000/predict_calories", {
gender: gender,
age: age,
height: height,
weight: weight,
duration: duration,
heart_rate: heart_rate,
body_temp: body_temp
}, function(data) {
$("#result-text").html("Estimated Calories Burnt: " + data.estimated_calories);
$("#result-card").fadeIn();
});
}
