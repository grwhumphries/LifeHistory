function CallIn(URL, Id) {
    $.ajax({
        url: URL,
        dataType: "html",
        success: function (data) {
            $(Id).html(data)
        }
    })


}


function cs() {
    var X = $('#commonSearch option:selected').val()
    var URL = '/commonname/?l='.concat(X);    
    var dURL = '/downloadCommon/?l='.concat(X);
    var downnum = ('<a href="').concat(dURL).concat('&DL=dlNum" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span>').concat(X).concat(' mass/morphology data</a>')
    var downchar = ('<a href="').concat(dURL).concat('&DL=dlChar" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span>').concat(X).concat(' Life history data</a>')
    var downcite = ('<a href="').concat(dURL).concat('&DL=dlCite" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span> Citations for ').concat(X).concat('</a>')

    $("#downloadnumeric").html(downnum);
    $("#downloadcharacter").html(downchar);
    $("#downloadcitations").html(downcite);
    CallIn(URL, "#searchresults")
}

function ss() {
    var X = $('#specSearch option:selected').val()
    var URL = '/species/?l='.concat(X);
    var dURL = '/downloadSpecies/?l='.concat(X);
    var downnum = ('<a href="').concat(dURL).concat('&DL=dlNum" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span>').concat(X).concat(' mass/morphology data</a>')
    var downchar = ('<a href="').concat(dURL).concat('&DL=dlChar" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span>').concat(X).concat(' Life history data</a>')
    var downcite = ('<a href="').concat(dURL).concat('&DL=dlCite" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span> Citations for ').concat(X).concat('</a>')
    $("#downloadnumeric").html(downnum);
    $("#downloadcharacter").html(downchar);
    $("#downloadcitations").html(downcite);
    CallIn(URL, "#searchresults")
}

function os() {
    var X = $('#orderSearch option:selected').val()
    var URL = '/order/?l='.concat(X);
    var dURL = '/downloadOrder/?l='.concat(X);
    var downnum = ('<a href="').concat(dURL).concat('&DL=dlNum" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span>').concat(X).concat(' mass/morphology data</a>')
    var downchar = ('<a href="').concat(dURL).concat('&DL=dlChar" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span>').concat(X).concat(' Life history data</a>')
    var downcite = ('<a href="').concat(dURL).concat('&DL=dlCite" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span> Citations for ').concat(X).concat('</a>')
    $("#downloadnumeric").html(downnum);
    $("#downloadcharacter").html(downchar);
    $("#downloadcitations").html(downcite);
    CallIn(URL, "#searchresults")
}

function fs() {
    var X = $('#familySearch option:selected').val()
    var URL = '/family/?l='.concat(X);
    var dURL = '/downloadFamily/?l='.concat(X);
    var downnum = ('<a href="').concat(dURL).concat('&DL=dlNum" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span>').concat(X).concat(' mass/morphology data</a>')
    var downchar = ('<a href="').concat(dURL).concat('&DL=dlChar" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span>').concat(X).concat(' Life history data</a>')
    var downcite = ('<a href="').concat(dURL).concat('&DL=dlCite" class="btn btn-info"><span class="glyphicon glyphicon-floppy-save"></span> Citations for ').concat(X).concat('</a>')
    $("#downloadnumeric").html(downnum);
    $("#downloadcharacter").html(downchar);
    $("#downloadcitations").html(downcite);
    CallIn(URL, "#searchresults")
}


function traitopts() {
    var X = $('#id_traits option:selected').val()
    var URL = '/chartraits/?ct='.concat(X);  
    CallIn(URL,"#div_id_traitopt")    
}


function OpenEdit() {
    var X = $('#specSearch option:selected').val()
    var URL = '/dbadd/?l='.concat(X);
    CallIn(URL,"#editfields")    
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



function getchartr() {    
    var X = event.srcElement.id;
    var Z = X.substring(0, (X.length - 4))
    var URL = '/charactertraits/?l='.concat(Z);
    var Y = '#'.concat(Z.replace(' ', '')).concat('char')
    $(Y).collapse('hide')
    $.ajax({
        url: URL,
        dataType: "html",
        success: function (data) {
            $(Y).html(data)            
        },

    }).done(function () {
        $(Y).collapse('show')
    })

    
    
};



function getnumtr() {    
    var X = event.srcElement.id;   
    var Z = X.substring(0, (X.length - 4))
    var URL = '/numerictraits/?l='.concat(Z);
    var Y = '#'.concat(Z.replace(' ', '')).concat('num')    
    $(Y).collapse('hide')
    $.ajax({
        url: URL,
        dataType: "html",
        success: function (data) {
            $(Y).html(data)
        },

    }).done(function () {
        $(Y).collapse('show')
    })
}






