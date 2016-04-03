# syloc

# Custom firebase-element
Temporarily installing HEAD of firebase-element
bower install GoogleWebComponents/firebase-element#0b1f9b9508dc30389fdbf9d93205cd179761ff07
until https://github.com/GoogleWebComponents/firebase-element/pull/109 is live


# Save an image in firebase (from console)
function toDataUrl(url, callback, outputFormat){
    var img = new Image();
    img.crossOrigin = 'Anonymous';
    img.onload = function(){
        var canvas = document.createElement('CANVAS');
        var ctx = canvas.getContext('2d');
        var dataURL;
        canvas.height = this.height;
        canvas.width = this.width;
        ctx.drawImage(this, 0, 0);
        dataURL = canvas.toDataURL(outputFormat);
        callback(dataURL);
        canvas = null;
    };
    img.src = url;
}
function loadScript(url, callback)
{
    // Adding the script tag to the head as suggested before
    var head = document.getElementsByTagName('head')[0];
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = url;

    // Then bind the event to the callback function.
    // There are several events for cross browser compatibility.
    script.onreadystatechange = callback;
    script.onload = callback;

    // Fire the loading
    head.appendChild(script);
}
loadScript('https://sykes-locations.appspot.com/components/firebase/firebase.js');
var ref = new Firebase('https://syloc.firebaseio.com/main/backgrounds/0');
toDataUrl('https://pixabay.com/get/e837b10728f1073ed1534705fb0938c9bd22ffd41db4184396f8c17ba6/young-woman-1208056_1920.jpg', function(base64Img){ ref.set(base64Img); });


# Initial setup (for posterity):
create app in github
create app in c9 from github link
create app.yaml
https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python
cd ~
wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.35.zip
unzip google_appengine_1.9.35.zip
rm google_appengine_1.9.35.zip
export PATH=$PATH:/home/ubuntu/google_appengine/
and add above .bashrc
/usr/bin/env python -V
https://cloud.google.com/appengine/docs/python/tools/uploadinganapp
appcfg.py update --noauth_local_webserver workspace
