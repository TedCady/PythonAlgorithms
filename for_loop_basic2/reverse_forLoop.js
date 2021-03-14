
function reverse (array){
    for (var i=0; i<array.length/2; i++){
        var temp=array[i];
        array[i]=array[array.length-1-i];
        array[array.length-1-i]=temp;
    }
    return array;
}

console.log(reverse([1,2,3,4,5,6]));