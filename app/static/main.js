var canvas;
var image;
var bThick = 20;
var cColour = '#FFFFFF'; // #black

//Initialize  fabric 
function initCanvas(){
    canvas = new fabric.Canvas('canvasBox');
    canvas.isDrawingMode = true;
    canvas.freeDrawingBrush.width = bThick;
    canvas.freeDrawingBrush.color = cColour;
    canvas.backgroundColor = '#000000';            
}

window.onload = function(){
    initCanvas();
};

//reset canvas
function reset() { 
    $('#guess').text('What is the number?');         
    canvas.clear();   
}

function handleImage(){                        
    var imgURL = canvas.toDataURL();   

    //Send Ajax call
    $.ajax({
        type: 'post',
        url: '/',
        data: {
            imageBase64 : imgURL
        },
    
        success: function(data){
            $('#guess').text(data.prediction);
        }              
    });                     
}