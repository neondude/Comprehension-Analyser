var quessetHttp = new XMLHttpRequest();
var quesAns = [];
var noq = 0; //number of questions
var score = 0; 
var count = 0;
var passageTime = 60000 * 5;
var passageTimeCopy = 60000 * 5;
var quesTime = 60000 * 2;
var countTime;

quessetHttp.onreadystatechange = function() {
    if (quessetHttp.readyState == 4 && quessetHttp.status == 200) {
        var myArr = JSON.parse(quessetHttp.responseText);
        displayQues(myArr.testlist.queslist);
        noq = myArr.testlist.queslist.length;
        console.log(myArr);
    }
};
quessetHttp.open("GET", urlQues, true);
quessetHttp.send();



function displayQues(arr) {
    var out = "";
    var i;
    for(i = 0; i < arr.length; i++) {
        quesAns[i]=arr[i].optans;
        j=i+1
        out += '<div class="qheader"> '+ '(' + j +')' + arr[i].questext + '</div>'
        out += '<input type="radio" value="A" name="q' + j +'"' + 'id="q'+ j +'"' + ' >' + "A)" + arr[i].opta + '<br>'
        out += '<input type="radio" value="B" name="q' + j +'"' + 'id="q'+ j +'"' + ' >' + "B)" + arr[i].optb + '<br>'
        out += '<input type="radio" value="C" name="q' + j +'"' + 'id="q'+ j +'"' + ' >' + "C)" + arr[i].optc + '<br>'
        out += '<input type="radio" value="D" name="q' + j +'"' + 'id="q'+ j +'"' + ' >' + "D)" + arr[i].optd + '<br><br>'
    }
    document.getElementById("quesset").innerHTML = out;
}



function evalQues(){
    clearInterval(countTime);
    var j = -1;
    var resultOut = ""
    for (q=1;q<=noq;q++){
        j= q-1;
        var quesDOM = eval("document.QuesContain.q"+q+".value");
        var quesVal = quesDOM;
        console.log("value for q="+q+"is: "+quesVal);
        if ((quesVal==undefined) || (quesVal==null) || (quesVal == "")){
            continue;
        }else{
            if(quesVal==quesAns[j]){
                score += getScore(q);
            }            
        }
    }
    document.getElementById("testView").style.display = "none";
    document.getElementById("submitBtn").style.display = "none";
    resultOut += "<h1>SCORE:" + score + "</h1>"
    resultOut += "<h2>Reading Speed:" + getReadingSpeed() + " words/min";
    document.getElementById("result").innerHTML = resultOut ;
    console.log("score is="+score);
}

function getScore(q){
    return 1;
}


function beginTest(){
    document.getElementById("testView").style.visibility = "visible";
    document.getElementById("submitBtn").style.visibility = "visible";
    document.getElementById("startBtn").style.display = "none";
    document.getElementById("tab-passage").checked = true;
    countTime = setInterval(timeElapsed,1000);
    
}

function timeElapsed(){
    count += 1;
    if(document.getElementById("tab-passage").checked == true){
        passageTime -= 1000;
        document.getElementById("tab-label-passage").innerHTML = "PASSAGE " + getTimeString(passageTime);
    }else{
        quesTime -= 1000;
        document.getElementById("tab-label-ques").innerHTML = "QUESTIONS " + getTimeString(quesTime);
    }
    
    if(passageTime<=0 || quesTime<=0){
        clearInterval(countTime);
        evalQues();
    }
    
}

function getTimeString(secIn){    
    var secs = Math.floor( (secIn/1000) % 60 ).toString();
    secs = ('0' + secs).slice(-2);
    var mins = Math.floor( (secIn/1000/60) % 60 ).toString();
    mins = ('0' + mins).slice(-2);
    return '('+mins+':'+secs+')';
    
}

function getReadingSpeed(){
    var readTime = (passageTimeCopy - passageTime)/1000
    console.log('readTime='+readTime+" nofwords="+noWords);
    rspeed = Math.floor(noWords/(readTime));
    return rspeed*60;
}

