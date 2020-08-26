function changeMode() {
	var coolerSpans =["cooler1Span","cooler2Span","cooler3Span","cooler4Span","cooler5Span","cooler6Span","cooler7Span","cooler8Span"];
	var coolerCheck =["cooler1Check","cooler2Check","cooler3Check","cooler4Check","cooler5Check","cooler6Check","cooler7Check","cooler8Check"];
	for (var i = 0; i < 8; i++){
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
	sendToArd();
}
function sendToArd() {
var coolerCheck =["cooler1Check","cooler2Check","cooler3Check","cooler4Check","cooler5Check","cooler6Check","cooler7Check","cooler8Check"];
var reader ="";
if(document.getElementById("ManualControl").checked){
reader = "33333333";
}
else{
for (var i = 0; i < 8; i++){
	if(document.getElementById(coolerCheck[i]).checked){
		reader = reader + "1";
	}
	else{
		reader = reader + "0";
}
	
}
}


var temp =  document.getElementById("targetTemp").value;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200 ) {
      document.getElementById("demo1").innerHTML =
      this.responseText;
	  console.log(this.responseText);
    }
  };

  xhttp.open("GET", "http://192.168.0.247:80/demo?coolerStates="+reader+"&temp="+temp , true);
  xhttp.send();
}