function changeMode(ip) {
	var coolerSpans =["cooler1Span","cooler2Span","cooler3Span","cooler4Span","cooler5Span","cooler6Span"];
	var coolerCheck =["cooler1Check","cooler2Check","cooler3Check","cooler4Check","cooler5Check","cooler6Check"];
	for (var i = 0; i < 6; i++){
		if (document.getElementById(coolerSpans[i]).classList.contains('slider')){

			document.getElementById(coolerSpans[i]).classList.remove('slider');

			document.getElementById(coolerSpans[i]).classList.add("slider-grey");

			document.getElementById(coolerCheck[i]).checked = false;

		}
		else
		{
			document.getElementById(coolerSpans[i]).classList.remove('slider-grey');
			document.getElementById(coolerSpans[i]).classList.add("slider");
			document.getElementById(coolerCheck[i]).checked = false;
		}
	}
	
	
	sendToArd(ip);
}
function sendToArd(ip) {

var coolerCheck =["cooler1Check","cooler2Check","cooler3Check","cooler4Check","cooler5Check","cooler6Check"];
var reader ="";
if(document.getElementById("manualControl").checked){
reader = "33333333";

}
else{	
for (var i = 0; i < 6; i++){
	if(document.getElementById(coolerCheck[i]).checked){
		reader = reader + "1";
	}
	else{
		reader = reader + "0";
}

}
}

var temp =  ""+document.getElementById("targetTemp").value;

if (temp[1] == "." || temp[1] == ","){

	temp = temp[0]+temp[2];
}

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200 ) {
      document.getElementById("demo1").innerHTML =
      this.responseText;
	  console.log(this.responseText);
    }
  };

  xhttp.open("GET", "http://"+ip+":80/demo?coolerStates="+reader+"&temp="+temp , true);
  xhttp.send();
}