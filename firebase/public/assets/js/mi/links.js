let linksWebSite = document.getElementById('linksWebSite')
let htmlLinks    = ''
let linkCity     = ''

for(let i = 0; i < 22; i++){
    let randomNumber     = getRandomArbitrary(0, CITIES.length-1)
    let USER_CITY        = CITIES[randomNumber].replaceAll('+', ' ')
    linkCity             = USER_CITY.replaceAll(' ', '+')  
    htmlLinks += '&nbsp;&nbsp;<a href="https://xboss.es/?city='+linkCity+'" style="color:grey;">'+USER_CITY+'</a>&nbsp;&nbsp;'
}

linksWebSite.innerHTML = htmlLinks+'<br><br><br>'
