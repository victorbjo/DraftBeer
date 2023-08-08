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
  client.subscribe('bekant/height', { qos: 0 })

})


client.on('message', (topic, message, packet) => {
  console.log('Received Message: ' + message.toString() + '\nOn topic: ' + topic)
  document.getElementById('height').innerHTML = message.toString()+" cm"
})
function publish(topic, message) {
  console.log('publishing', topic, message)
  if (client.connected == true) {
    client.publish(topic, message, options)
    console.log('published', topic, message)
  }
}
