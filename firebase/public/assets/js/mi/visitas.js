var firebaseConfig = {
    apiKey: "AIzaSyDZ6cpfLEHB6YTN_C1UXw5dpaOuO3041s8",
    authDomain: "x-route-planning.firebaseapp.com",
    databaseURL: "https://x-route-planning-default-rtdb.firebaseio.com",
    projectId: "x-route-planning",
    storageBucket: "x-route-planning.appspot.com",
    messagingSenderId: "536796594344",
    appId: "1:536796594344:web:bfff3ae5a787d1a457029d",
    measurementId: "G-VHTNMZ1N44"
}

window.onload = function(){
    firebase.initializeApp(firebaseConfig)
    var databaseFirebase = firebase.database()

    // read data
    databaseFirebase.ref('users/visited').on('value', (snapshot) => {
        var objVisits = snapshot.val()
        let spanVisitas =  document.getElementById('spanVisitas')
        if(spanVisitas){
            spanVisitas.innerText = objVisits.v
        }
        objVisits.v++
        console.log('visitas='+objVisits.v)

        let userCounted = window.localStorage.getItem('counted') || false
        if(!userCounted){
            // put data
            window.localStorage.setItem('counted', 'counted')
            databaseFirebase.ref('users/visited').set({ v: objVisits.v })
        }
    })
}