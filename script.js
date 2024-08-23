var outList = [];
var count = 0;
var found = false;
var logList = [];

document.getElementById("button1").addEventListener("click", function() {
    var id = document.getElementById("text_input1").value;
    var timeStamp = new Date().toUTCString();
    
    if (id != "") {
        if (count == 0 ) {
            outList.push(id);
            logList.push(id + " Depart " + timeStamp);
            document.getElementById("text_area2").value = "Left to Restroom\n" + timeStamp;
            count++;
        } else {
            for (var i = 0; i < outList.length; i++) {
                if (id == outList[i]) {
                    document.getElementById("text_area2").value = "Returned from Restroom\n" + timeStamp;
                    logList.push(id + " Return " + timeStamp);
                    outList.splice(i, 1);
                    found = true;
                    count--;
                }
            }
            if (!found) {
                outList.push(id);
                logList.push(id + " Depart " + timeStamp);
                document.getElementById("text_area2").value = "Left to Restroom\n" + timeStamp;
                count++;
            }
            found = false;
        }
    } else {
        document.getElementById("text_area2").value = "Please input ID to continue";
    }
    document.getElementById("text_input1").value = "";
});

function downloadLog() {
    var logString = logList.join('\n');
    var blob = new Blob([logString], { type: 'text/plain' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.download = 'Log.txt';
    a.href = url;
    a.click();
    URL.revokeObjectURL(url);
}

document.getElementById("button2").addEventListener("click", function() {
    downloadLog();
});
