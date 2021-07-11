  function Predict_Covid() {
    console.log("Predict button clicked");
    var breath_prob2 = document.getElementById("breath_prob").value;
    var fever2 = document.getElementById("fever").value;
    var drycough2 = document.getElementById("drycough").value;
    var sorethroat2 = document.getElementById("sorethroat").value;
    var hyperTension2 = document.getElementById("hyperTension").value;
    var abroadtravel2 = document.getElementById("abroadtravel").value;
    var contact2 = document.getElementById("contact").value;
    var largeGathering2 = document.getElementById("largeGathering").value;
    var publicExposedPlaces2 = document.getElementById("publicExposedPlaces").value;
    var familyPublicPlaces2 = document.getElementById("familyPublicPlaces").value;
    var output2 = document.getElementById("output");
  
    var url = "http://127.0.0.1:5000/predict_covid1"; 
  
    $.post(url, {
        breath_prob1:breath_prob2,
        fever1:fever2,
        drycough1:drycough2,
        sorethroat1:sorethroat2,
        hyperTension1:hyperTension2,
        abroadtravel1:abroadtravel2,
        contact1:contact2,
        largeGathering1:largeGathering2,
        publicExposedPlaces1:publicExposedPlaces2,
        familyPublicPlaces1:familyPublicPlaces2
    },function(data, status) {
        console.log(data.prediction);
        output2.innerHTML = "<h5><b>"+data.prediction.toString()+"<h5></b>";
        console.log(status);
    });
  }
