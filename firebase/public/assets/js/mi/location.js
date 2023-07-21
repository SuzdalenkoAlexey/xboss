let URL_PAGE   = window.location.href.split('?city=')
let DIV_IMAGES = document.getElementById('porfolioItemImage')
let IMAGE_URL  = ''
let ALT_DESCR  = ''
var TITLE_PAGE = ''
var H1_TITLE   = document.getElementById('titlePageText')
var USER_CITY  = 'Madrid'

if(URL_PAGE[1] == undefined || !URL_PAGE[1]){  
    let randomNumber     = getRandomArbitrary(0, CITIES.length-1)
    USER_CITY            = CITIES[randomNumber].replaceAll('+', ' ')
    // window.location.href = '?city='+place
    document.getElementById('sectionSubtitle').innerHTML = USER_CITY
    document.getElementById('sectionTitleMb').innerHTML  = 'Diseño Web '+USER_CITY
    TITLE_PAGE = USER_CITY.replaceAll('+', ' ')
} else {
    TITLE_PAGE = URL_PAGE[1].replaceAll('+', ' ')
    document.title     = 'Diseño Web '+TITLE_PAGE
    document.getElementsByTagName('meta')["keywords"].content = 'Diseño Web '+TITLE_PAGE
    document.getElementsByTagName('meta')["description"].content = 'Diseño Web '+TITLE_PAGE
    H1_TITLE.innerText = 'Diseño Web '+TITLE_PAGE
    document.getElementById('sectionSubtitle').innerHTML = TITLE_PAGE
    document.getElementById('sectionTitleMb').innerHTML  = 'Diseño Web '+TITLE_PAGE
    USER_CITY = URL_PAGE[1].replaceAll(' ', '+')
}

getImages()




function getImages(){
    fetch('https://imagedeveloper.pythonanywhere.com/?city='+USER_CITY.replaceAll(' ', '+')).then(res => res.json()).then(result => {
        let htmlImages = ''
        let srcImg     = ''
        result.images.forEach(image => {
            srcImg     = 'https://imagedeveloper.pythonanywhere.com/show_image/'+image
            htmlImages +=  `<div class="col-md-4">
                                <a href="/image/?city=`+USER_CITY.replaceAll(' ', '+')+`" class="portfolio-card">
                                    <img src="`+srcImg+`" class="portfolio-card-img" alt="`+TITLE_PAGE+`">    
                                    <span class="portfolio-card-overlay">
                                        <span class="portfolio-card-caption">
                                            <h4>`+TITLE_PAGE+`</h5>
                                            <p class="font-weight-normal">Diseño Web `+TITLE_PAGE+`</p>
                                        </span>                         
                                    </span>                     
                                </a>
                            </div>`
        })
        DIV_IMAGES.innerHTML = htmlImages
        window.localStorage.setItem('error', 0)
    }).catch(e => {
        let miError = window.localStorage.getItem('error')
        if(miError < 5){
            miError++
            window.localStorage.setItem('error', miError)
            window.location.href = '/'
        }
       

        
    })
}


let listImagesPage = document.getElementsByTagName('img')
for(let imgHtml of listImagesPage){ imgHtml.alt = 'Diseño Web '+TITLE_PAGE; }