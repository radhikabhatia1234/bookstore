function viewbooks(obj) {
    alert(obj);
    var xml=new XMLHttpRequest();
    xml.onreadystatechange=function () {
      if (this.status==200 && this.readyState==4){
          var output=this.response;
          alert(output);
      }
    };
    xml.open('GET','',true);
    xml.send()
}