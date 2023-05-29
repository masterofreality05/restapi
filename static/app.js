async function listCupcakes() {
    let newItem =  await axios.get(`http://localhost:5000/api/cupcakes`)
    console.log(newItem)
    let listedCupcakes = []

    for(item of newItem.data.cupcakes){
       console.log(item.flavor)
       listedCupcakes.push(item.flavor)



   $('#returned').text(listedCupcakes)
    }
    


}
 
 
 async function getcupcakes() {
   
    let val = $('#idinput').val()
    let newItem =  await axios.get(`http://localhost:5000/api/cupcakes/${val}`)
  
    $('#returned').text(newItem.data.cupcake.flavor)


}

async function createCupcake() {

    let flavor = $('#flavor').val()
    let size = $('#size').val()
    let rating = $('#rating').val()
    let image = $('#image').val()


    let newItem =  await axios.post(`http://localhost:5000/api/cupcakes`, {"flavor": flavor, "size": size,
    "rating": rating, "image": image})

    console.log(newItem)
    listCupcakes()




}
