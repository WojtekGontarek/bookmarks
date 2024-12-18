const siteUrl = '//127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250
const minHeight = 250

const head = document.getElementsByTagName('head')[0];
const link = document.createElement("link");
link.rel = "stylesheet";
link.type = "text/css";
link.href = siteUrl + '?r=' + Math.floor(Math.random() * 9999999999999);
head.appendChild(link);

const body = document.getElementsByTagName('body')[0];
boxHtml = `
    <div id="bookmarklet">
        <a href="#" id="close">&times;</a>
        <h1>Wybierz zdjecie do zapisania:</h1>
        <div class="images"></div>
    </div>
`
box.innerHTML += boxHtml;

function bookmarkletLaunch(){
    bookmarklet = document.getElementById('bookmarklet');
    const imagesFound = document.querySelector(".images");
    imagesFound.innerHTML = '';
    bookmarklet.style.display = 'block';

    bookmarklet.getElementById('close').addEventListener('click', function(){
        bookmarklet.style.display = 'none';
    });

    images = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]');
    images.forEach(image => {
        if (image.naturalWidth >= minWidth && image.naturalHeight >= minHeight) {}
    })
}

bookmarkletLaunch();