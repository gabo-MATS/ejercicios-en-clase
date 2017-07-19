

var a = 20;
var h = "* ";
var e = " ";

for (i = 0 ; i < a; i++){
	var p=i-1;
	console.log(e.repeat(a-p) + h.repeat(i));

}

console.log(e.repeat(a) + "* ")
