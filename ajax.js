
function ajax(url, data, successFunction) {
    var showStatus = false;
    function completeFn() {
        if (showStatus) {
//        console.log("complete");
            $("#ajaxstatus").html("");
        }
    }
    
    function successFn() {
        if (showStatus) {
//        console.log("success");
            $("#ajaxstatus").html("success");
        }
    }
    
    function errorFn() {
        if (showStatus) {
//        console.log("error");
            $("#ajaxstatus").html("error");
        }
    }
    
    $("#ajaxstatus").html("loading");
    
    var jqxhr = $.post(url, data, successFunction)
        .complete(completeFn)
        .success(successFn)
        .error(errorFn);
}
