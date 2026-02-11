document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("diabetes").style.display = "block";
});
function openPrediction(evt, predictionName) {
    var i, prediction, tablinks;
    prediction = document.getElementsByClassName("prediction");
    for (i = 0; i < prediction.length; i++) {
        prediction[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(predictionName).style.display = "block";
    evt.currentTarget.className += " active";
}

function validateForm(event) {
    var inputs = event.target.getElementsByTagName("input");
    var selects = event.target.getElementsByTagName("select");
    var isValid = true;

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].value === "") {
            isValid = false;
            break;
        }
    }

    if (isValid) {
        for (var j = 0; j < selects.length; j++) {
            if (selects[j].value === "") {
                isValid = false;
                break;
            }
        }
    }

    if (!isValid) {
        alert("Please fill in all the fields.");
        event.preventDefault();
    }
}
