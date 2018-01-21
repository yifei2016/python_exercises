function findBiggerThan10(list){
  var result = undefined;
  for(var i =0;i<list.length;i++){
    if(list[i] > 10){
      result = list[i];
      break;
    }
  }
  return result;
}

function find(list, testing_function){
  var result = undefined;
  
  for(var i =0;i<list.length;i++){
    if(testing_function(list[i]) === true){
      result = list[i];
      break;
    }
  }
  return result;
}

find([1,20],function(element){
  return element > 10;
})


function map(list, mapper){
  var result =[];

  for(var i = 0; i<list.length;i++){
    result.push( mapper(list[i]) )
  }
 return result;
}
var fn = function(e){
  return e*2;
}
map([1,2,3],fn )


function filter(list, filt){
  var result = [];
  for(var i =0; i<list.length;i++){
    if(filt(list[i]) === true){
      result.push(list[i]);
    }
  }
  return result;
}

var fn = function(e){
  return e.length > 6;
}
filter(["yifeisdf", "chuan"],fn )

function findIndex(list,findI){
  var result = -1;
  for(var i = 0;i<list.length;i++){
    if(findI(list[i]) === true){
      result = i;
      break;
    }
  }
  return result;
}



[2,34,14].findIndex(function(e){
  return e > 13;
})

a = new Array(1,2,3)
[ 1, 2, 3 ]

Array.prototype.findIndex = function(findI){
  console.log("yifei function")
  var result = -1;
  for(var i = 0;i<this.length;i++){
    if(findI(this[i]) === true){
      result = i;
      break;
    }
  }
  return result;
}
