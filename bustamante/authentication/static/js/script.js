var img = new Image();

// Variables de usuario - personalizar estas para cambiar la imagen cuando inicie el desplazamiento
// dirección y velocidad.

img.src = 'https://static.vecteezy.com/system/resources/previews/000/683/635/non_2x/textured-vector-plaid-pattern-background.jpg';
var CanvasXSize = 1920;
var CanvasYSize = 80;
var speed = 30; //más bajo es más rápido
var scale = 1.00;
var y = -4.5; //desplazamiento vertical

// Programa principal

var dx = 0.75;
var imgW;
var imgH;
var x = 0;
var clearX;
var clearY;
var ctx;

function maquillar() {
    var canball = document.getElementById('canvas');
    canball.style = 'width:100%; height: 10px';

}

function mostrar() {
    document.getElementById("div_seccion").innerHTML = "";
    console.clear();
    cargarDatos();
}

img.onload = function() {
    imgW = img.width * scale;
    imgH = img.height * scale;

    if (imgW > CanvasXSize) {
        // imagen más grande que canvas
        x = CanvasXSize - imgW;
    }
    if (imgW > CanvasXSize) {
        // ancho de imagen más grande que canvas
        clearX = imgW;
    } else {
        clearX = CanvasXSize;
    }
    if (imgH > CanvasYSize) {
        // altura de la imagen más grande que canvas
        clearY = imgH;
    } else {
        clearY = CanvasYSize;
    }

    // obtener contexto de canvas
    ctx = document.getElementById('canvas').getContext('2d');

    // establecer frecuencia de actualización
    return setInterval(draw, speed);
}

function draw() {
    ctx.clearRect(0, 0, clearX, clearY); // clear the canvas

    // si la imagen es <= tamaño de Canvas
    if (imgW <= CanvasXSize) {
        // reiniciar, comenzar desde el principio
        if (x > CanvasXSize) {
            x = -imgW + x;
        }
        // dibujar image1 adicional
        if (x > 0) {
            ctx.drawImage(img, -imgW + x, y, imgW, imgH);
        }
        // dibujar image2 adicional
        if (x - imgW > 0) {
            ctx.drawImage(img, -imgW * 2 + x, y, imgW, imgH);
        }
    }

    // la imagen es > tamaño de Canvas
    else {
        // reiniciar, comenzar desde el principio
        if (x > (CanvasXSize)) {
            x = CanvasXSize - imgW;
        }
        // dibujar image adicional
        if (x > (CanvasXSize - imgW)) {
            ctx.drawImage(img, x - imgW + 1, y, imgW, imgH);
        }
    }
    // dibujar imagen
    ctx.drawImage(img, x, y, imgW, imgH);
    // cantidad para moverse
    x += dx;
}

function cargarDatos() {

    //Igresa datos del json (905)
    for (i = 0; i < 905; i++) {
        /*---------------------Extraer API----------------------*/
        fetch('https://pokeapi.co/api/v2/pokemon/' + (i + 1) + '/')
            .then(res => res.json())
            .then(res => {
                var dataJson = (res);
                //var dataJson = JSON.parse(JSON.stringify(res));
                console.log(res);
                /*-------------------------------Generar Seccion-------------------------------*/
                var div_seccion = document.getElementById('div_seccion');
                var div_interno = document.createElement("div");
                var div_interno_der = document.createElement("div");
                var div_interno_izq = document.createElement("div");
                div_interno.style = 'padding-bottom:5em;';
                div_interno_der.style = 'width:79%; float:right; display:inline-block;';
                div_interno_izq.style = 'width:19%; float:left; display:inline-block;';
                div_seccion.appendChild(div_interno);
                div_interno.appendChild(div_interno_der);
                div_interno.appendChild(div_interno_izq);

                /*------------------------------Nombre------------------------------*/
                var palabra = document.createTextNode(dataJson.name);
                var Nombre = document.createElement("h2");
                Nombre.style = 'font-family:verdana;';
                Nombre.appendChild(palabra);
                div_interno_izq.appendChild(Nombre);

                /*-------------------------------Tabla-------------------------------*/
                var tabla = document.createElement("table");
                div_interno_der.appendChild(tabla);

                /*------------------------------fila 1 ENCABEZADOS------------------------------*/
                //crea una fila
                var tr = document.createElement("tr");

                //encabezado Peso
                var th = document.createElement("th");
                var encabezado_peso = document.createTextNode("Peso");
                tabla.appendChild(tr);
                tr.appendChild(th);
                th.appendChild(encabezado_peso);

                //encabezado Altura
                var th = document.createElement("th");
                var encabezado_altura = document.createTextNode("Altura");
                tabla.appendChild(tr);
                tr.appendChild(th);
                th.appendChild(encabezado_altura);

                //encabezado Experiencia
                var th = document.createElement("th");
                var encabezado_experiencia = document.createTextNode("Experiencia");
                tabla.appendChild(tr);
                tr.appendChild(th);
                th.appendChild(encabezado_experiencia);

                /*------------------------------fila 2 CONTENIDO------------------------------*/
                //crea una fila
                var tr = document.createElement("tr");

                var td = document.createElement("td");
                //IMPORTANTE
                var valor_peso = document.createTextNode(dataJson.weight);
                tabla.appendChild(tr);
                tr.appendChild(td);
                //IMPORTANTE
                td.appendChild(valor_peso);

                var td = document.createElement("td");
                //IMPORTANTE
                var valor_altura = document.createTextNode(dataJson.height);
                tabla.appendChild(tr);
                tr.appendChild(td);
                //IMPORTANTE
                td.appendChild(valor_altura);

                var td = document.createElement("td");
                //IMPORTANTE
                var valor_experiencia = document.createTextNode(dataJson.base_experience);
                tabla.appendChild(tr);
                tr.appendChild(td);
                //IMPORTANTE
                td.appendChild(valor_experiencia);
            }); //fin del fetch
    } //fin del for
}


//fin del programa