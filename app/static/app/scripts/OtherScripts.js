
function gettraits() {
    var X = event.srcElement.id;    
    var Xx = X.replace(" ", "%20")

    var did = X.replace(" ","")
    var DivId = ('#').concat(did).concat('div')
    
    var URL = '/gettraits/?t='.concat(Xx);
    

    $.ajax({
        url: URL,
        dataType: "html",
        success: function (data) {
            $(DivId).html(data)
        }
    })

}



function cs() {
    var X = $('#commonSearch option:selected').val()
    var URL = '/commonname/?l='.concat(X);
    var dURL = '/downloadCommon/?l='.concat(X);
    var down = ('<a href="').concat(dURL).concat('" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span> Download ').concat(X).concat(' as CSV</a>')
    $("#downloadbutton").html(down);
    dataload(URL)
}

function ss() {
    var X = $('#specSearch option:selected').val()
    var URL = '/species/?l='.concat(X);
    var dURL = '/downloadSpecies/?l='.concat(X);
    var down = ('<a href="').concat(dURL).concat('" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span> Download ').concat(X).concat(' as CSV</a>')
    $("#downloadbutton").html(down);
    dataload(URL)
}

function os() {
    var X = $('#orderSearch option:selected').val()
    var URL = '/order/?l='.concat(X);
    var dURL = '/downloadOrder/?l='.concat(X);
    var down = ('<a href="').concat(dURL).concat('" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span> Download ').concat(X).concat(' as CSV</a>')
    $("#downloadbutton").html(down);
    dataload(URL)
}

function fs() {
    var X = $('#familySearch option:selected').val()
    var URL = '/family/?l='.concat(X);
    var dURL = '/downloadFamily/?l='.concat(X);
    var down = ('<a href="').concat(dURL).concat('" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span> Download ').concat(X).concat(' as CSV</a>')
    $("#downloadbutton").html(down);
    dataload(URL)
}



function traitopts() {
    var X = $('#id_traits option:selected').val()
    var URL = '/chartraits/?ct='.concat(X);
    
    $.ajax({
        url: URL,
        dataType: "html",
        success: function (data) {
            $("#div_id_traitopt").html(data);            
        }
    });    
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
        url: '/dbadd/',
        dataType: "html",
        success: function (data) {
            $(".viewwindow").html(data);
        }
    });
}

function OpenAddother() {
    //JQuery AJax
    $.ajax({
        url: '/dbaddother/',
        dataType: "html",
        success: function (data) {
            $(".viewwindow").html(data);
        }
    });
}



function OpenEdit() {
    var X = $('#specSearch option:selected').val()
    var URL = '/dbadd/?l='.concat(X);

    $.ajax({
        url: URL,
        dataType: "html",
        success: function (data) {
            $("#editfields").html(data);
        }
    });
}







jQuery.fn.tableToCSV = function () {

    var clean_text = function (text) {
        text = text.replace(/"/g, '""');
        return '"' + text + '"';
    };

    $(this).each(function () {
        var table = $(this);
        var caption = $(this).find('caption').text();
        var title = [];
        var rows = [];

        $(this).find('tr').each(function () {
            var data = [];
            $(this).find('th').each(function () {
                var text = clean_text($(this).text());
                title.push(text);
            });
            $(this).find('td').each(function () {
                var text = clean_text($(this).text());
                data.push(text);
            });
            data = data.join(",");
            rows.push(data);
        });
        title = title.join(",");
        rows = rows.join("\n");

        var csv = title + rows;
        var uri = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv);
        var download_link = document.createElement('a');
        download_link.href = uri;
        var ts = new Date().getTime();
        if (caption == "") {
            download_link.download = ts + ".csv";
        } else {
            download_link.download = caption + "-" + ts + ".csv";
        }
        document.body.appendChild(download_link);
        download_link.click();
        document.body.removeChild(download_link);
    });

};


function download() {
    var f = event.srcElement.id;
    var tab = '#'.concat(f);
    $(tab).tableToCSV();
}