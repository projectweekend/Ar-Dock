var jackrabbit = require( "jackrabbit" );
var serialport = require( "serialport" );
var syslog = require( "syslog" );


var serialAddress = process.env.SERIAL_ADDRESS;
var serialRate = process.env.SERIAL_RATE;
var rabbitURL = process.env.RABBIT_URL;


var broker = jackrabbit( rabbitURL, 1 );

var serialPort = new serialport.SerialPort( serialAddress, {
    baudrate: serialRate,
    parser: serialport.parsers.readline( "\n" )
} );

var logger = syslog.createClient( 514, "localhost" );

var serialDataToJSON = function ( sensorData ) {
    var output = {};
    sensorData.split( "|" ).map( function ( sensorReading ) {
        var parts = sensorReading.split( ":" );
        output[ parts[ 0 ] ] = parseFloat( parts[ 1 ] );
    } );
    return JSON.stringify( output );
};

var brokerOnReady = function ( err, queue, info ) {
    logger.info( "Env-Sensor | Broker ready" );
    if ( err ) {
        logger.error( "Env-Sensor | Error with 'brokerOnReady': " + err );
        process.exit( 1 );
    }
    broker.handle( "sensor.get", function ( message, ack ) {
        serialPort.on( "data", function ( data ) {
            ack( serialDataToJSON( data ) );
        } );
        serialPort.write( message.serialMessage, function ( err, data ) {
            if ( err ) {
                logger.error( "Env-Sensor | Error with 'serialPort.write': " + err );
                process.exit( 1 );
            }
        } );
    } );
};

var brokerOnConnect = function () {
    logger.info( "Env-Sensor | Broker connected" );
    broker.create( "sensor.get", { prefetch: 5 }, brokerOnReady );
};

// Kick it off when serial port is open
serialPort.on( "open", function () {
    logger.info( "Env-Sensor | Serial port open" );
    broker.on( "connected", brokerOnConnect );
} );

serialPort.on( "error", function ( err ) {
    logger.error( "Env-Sensor | Error event 'serialPort': " + err );
    process.exit( 1 );
} );

broker.on( "disconnected", function () {
    logger.error( "Env-Sensor | Error 'broker' disconnected" );
    process.exit( 1 );
} );
