var utils = require( "./utils" );


var broker = utils.jackrabbit();
var serialPort = utils.serialport();
var logger = utils.logger( [ "environmental-sensor-service" ] );

var serialDataToJSON = function ( sensorData ) {
    var output = {
        date: new Date()
    };
    sensorData.split( "|" ).map( function ( sensorReading ) {
        var parts = sensorReading.split( ":" );
        output[ parts[ 0 ] ] = parseFloat( parts[ 1 ] );
    } );
    return JSON.stringify( output );
};

var brokerOnReady = function ( err, queue, info ) {
    logger.log( "Broker ready" );
    if ( err ) {
        logger.log( "Error with 'brokerOnReady': " + err );
        process.exit( 1 );
    }
    broker.handle( "sensor.get", function ( message, ack ) {
        serialPort.on( "data", function ( data ) {
            ack( serialDataToJSON( data ) );
        } );
        serialPort.write( message.serialMessage, function ( err, data ) {
            if ( err ) {
                logger.log( "Error with 'serialPort.write': " + err );
                process.exit( 1 );
            }
        } );
    } );
};

var brokerOnConnect = function () {
    logger.log( "Broker connected" );
    broker.create( "sensor.get", { prefetch: 5 }, brokerOnReady );
};

// Kick it off when serial port is open
serialPort.on( "open", function () {
    logger.log( "Serial port open" );
    broker.on( "connected", brokerOnConnect );
} );

serialPort.on( "error", function ( err ) {
    logger.log( "Error event 'serialPort': " + err );
    process.exit( 1 );
} );

broker.on( "disconnected", function () {
    logger.log( "Error 'broker' disconnected" );
    process.exit( 1 );
} );
