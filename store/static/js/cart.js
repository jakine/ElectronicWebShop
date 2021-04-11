var updatebutton = document.getElementsByClassName('update-cart')
for(var i =0; i< updatebutton.length; i++){
    updatebutton[i].addEventListener('click', function(){
       var product_id = this.dataset.product;
       var action = this.dataset.action;
       console.log('product_id', product_id, 'action', action)


       console.log('user', user)

       if (user === 'AnonymousUser'){
           console.log('Not logged in')
       } else {
           //console.log('User is logged in')
           updateUserOrder(product_id, action)
       }
    });

}


function updateUserOrder(productId, action){
    console.log('updating')

    var url='/updateitem/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })

    // give a response
    .then((response) =>{
        return response.json()
    })


    .then((data) => {
        console.log('data', data);
        location.reload();
    })
}