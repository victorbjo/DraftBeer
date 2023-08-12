const clientId = 'mqttjs_' + Math.random().toString(16).substr(2, 8)
//https://dev.to/emqx/connect-to-mqtt-broker-with-websocket-14do
const host = 'mqtt://212.10.203.7:9001'
const options = {
  keepalive: false,
  clientId: clientId,
  protocolId: 'MQTT',
  protocolVersion: 5,
  clean: true,
  reconnectPeriod: 100000,
  connectTimeout: 30 * 1000,
  will: {
    topic: 'table',
    payload: 'Connection Closed abnormally..!',
    qos: 0,
    retain: false
  },
}

const client = mqtt.connect(host, options)

client.on('error', (err) => {
  console.log('Connection error: ', err)
  client.end()
})

client.on('reconnect', () => {
  console.log('Reconnecting...')
})
client.on('connect', () => {
  console.log('Client connected:' + clientId)
  // Subscribe
})


client.on('message', (topic, message, packet) => {
  console.log('Received Message: ' + message.toString() + '\nOn topic: ' + topic)
  if (topic == 'draft/temp'){
    update_temp(message.toString());
  }

  //document.getElementById('height').innerHTML = message.toString()+" cm"
})
function publish(topic, message) {
  console.log('publishing', topic, message)
  if (client.connected == true) {
    client.publish(topic, message, options)
    console.log('published', topic, message)
  }
}
function update_temp(msg){
  alert(msg);
}
function set_target(){
  var target = document.getElementById("target_temp").value;
  var message = '{"temp_target":"'+target+'","temp_cooler":"10","temp_hotside":"11","temp_ambient":"12"}'
  //alert(JSON.parse(message).temp_target);
  publish("draft/temp", message);
}