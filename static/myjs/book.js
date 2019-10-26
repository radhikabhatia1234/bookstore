function viewbooks(obj) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.status == 200 && this.readyState == 4) {
            var data = JSON.parse(this.response);
            var s = "";
            var output = data['x'];
            for (var i = 0; i < output.length; i++) {
                s += "<tr>";
                s += "<td>" + (i + 1) + "</td>";
                s += "<td>" + output[i]['title'] + "</td>";
                s += "<td>" + output[i]['description'] + "</td>";
                s += "<td>" + output[i]['price'] + "</td>";
                s += "<td>" + output[i]['edition'] + "</td>";
                s += "<td>" + output[i]['author'] + "</td>";
                s += "<td>" + output[i]['genre'] + "</td>";
                s += "<td>" + output[i]['category'] + "</td>";
                s += "<td><img src='static/media/" + output[i]['photo'] + "' alt='' width='100'></td>";
                s += "<td><button type='button' class='btn text-danger' onclick='editbook(" + output[i]['id'] + ")'><i class='fa fa-trash fa-2x'></i></button></td>";
                // s += "<td><a href='editbook?id=" + output[i]['id'] + "' class='btn text-warning'><i class='fa fa-edit fa-2x'></i></a></td>";
                s += "<td><button type='button' class='btn text-danger' onclick='deletebooks(" + output[i]['id'] + ")'><i class='fa fa-trash fa-2x'></i></button></td>";
                s += "</tr>";
            }
            document.getElementById("viewbookdata").innerHTML = s;
        }
    };
    xml.open('GET', 'viewbooks?catname=' + obj, true);
    xml.send();
}

function deletebooks(id) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var output = this.response;
            alert(output);
            window.location.href = "booksview"
        }
    };
    xml.open('GET', 'deltebooks?id=' + id, true);
    xml.send();
}

function editbook(id) {
    var xml = new XMLHttpRequest();
    xml.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
                var output = JSON.stringify(this.response);
                alert(output);
                // window.location.href = "bookview"
    }
};
xml.open('GET', 'editbook?id=' + id, true);
xml.send();
}