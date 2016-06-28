
function cs() {
    var X = $('#commonSearch option:selected').val()
    var URL = '/commonname/?l='.concat(X);    
    dataload(URL)
}

function ss() {
    var X = $('#specSearch option:selected').val()
    var URL = '/species/?l='.concat(X);    
    dataload(URL)
}

function os() {
    var X = $('#orderSearch option:selected').val()
    var URL = '/order/?l='.concat(X);   
    dataload(URL)
}

function fs() {
    var X = $('#familySearch option:selected').val()
    var URL = '/family/?l='.concat(X);    
    dataload(URL)
}


function dataload(URL) {
    
    $.ajax({
        url: URL,
        dataType: "html",
        success: function (data) {
            $("#searchresults").html(data)
        }
    })
}


function OpenSearch() {
    //JQuery AJax
    $.ajax({
        url: '/dbsearch',
        dataType: "html",
        success: function (data) {            
            $(".viewwindow").html(data);
        }
    });
}

function OpenAdd() {
    //JQuery AJax
    $.ajax({
        url: '/admin',
        dataType: "html",
        success: function (data) {
            $(".viewwindow").html(data);
        }
    });
}