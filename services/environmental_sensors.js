var jackrabbit = require( "jackrabbit" );
var serialport = require( "serialport" );


var serialAddress = process.env.SERIAL_ADDRESS;
var serialRate = process.env.SERIAL_RATE;
var rabbitURL = process.env.RABBIT_URL;


var broker = jackrabbit( rabbitURL, 1 );
var serialPort = new serialport.SerialPort( serialAddress, {
    baudrate: serialRate,
    parser: serialport.parsers.readline( "\n" )
} );

var parseSensorData = function ( sensorData ) {
    var output = {};
    sensorData.split( "|" ).map( function ( sensorReading ) {
        var parts = sensorReading.split( ":" );
        output[ parts[ 0 ] ] = parseFloat( parts[ 1 ] );
    } );
    return output;
};

var brokerOnReady = function () {
    broker.handle( "sensor.get", function ( message, ack ) {
        serialPort.on( "data", function ( data ) {
            ack( data );
        } );
        serialPort.write( message.serialMessage, function ( err, data ) {
            if ( err ) {
                console.log( "Error writing to serial port: " + err );
            }
        } );
    } );
};

var brokerOnConnect = function () {
    broker.create( "sensor.get", { prefetch: 5 }, brokerOnReady );
};

// Kick it off when serial port is open
serialPort.on( "open", function () {
    broker.on( "connected", brokerOnConnect );
} );
