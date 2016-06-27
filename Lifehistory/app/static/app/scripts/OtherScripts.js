function speciesSearch() {



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
        url: '/dbadd',
        dataType: "html",
        success: function (data) {
            $(".viewwindow").html(data);
        }
    });
}