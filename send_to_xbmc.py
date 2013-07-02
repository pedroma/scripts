import sys, requests, SimpleHTTPServer, SocketServer

AVTRANSPORT_URI = "http://127.0.0.1:58609/AVTransport/97281f3d-39b4-57f4-e8b3-956f1beb3a7c/control.xml"

HEADERS = {
    "Content-type":"text/xml;charset=\"utf-8\"",
    "Connection": "Keep-Alive",
    "Soapaction":"", # set this before making the request
}

STOP_PAYLOAD = """
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
    <s:Body>
        <u:Stop xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
            <InstanceID>0</InstanceID>
        </u:Stop>
    </s:Body>
</s:Envelope>
"""

SET_FILE_PAYLOAD = """
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
    <s:Body>
        <u:SetAVTransportURI xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
            <InstanceID>0</InstanceID>
            <CurrentURI>http://127.0.0.1:8902/%s</CurrentURI>
            <CurrentURIMetaData></CurrentURIMetaData>
        </u:SetAVTransportURI>
    </s:Body>
</s:Envelope>
"""

PLAY_PAYLOAD = """
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
    <s:Body>
        <u:Play xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
            <InstanceID>0</InstanceID>
            <Speed>1</Speed>
        </u:Play>
    </s:Body>
</s:Envelope>
"""

PORT = 8902
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

def main(play_file):
    HEADERS.update({"Soapaction":"\"urn:schemas-upnp-org:service:AVTransport:1#Stop\""})
    requests.post(AVTRANSPORT_URI, headers=HEADERS,data=STOP_PAYLOAD) # STOP playing
    HEADERS.update({"Soapaction":"\"urn:schemas-upnp-org:service:AVTransport:1#SetAVTransportURI\""})
    requests.post(AVTRANSPORT_URI, headers=HEADERS,data=SET_FILE_PAYLOAD%play_file)
    httpd.serve_forever()
    HEADERS.update({"Soapaction":"\"urn:schemas-upnp-org:service:AVTransport:1#Play\""})
    requests.post(AVTRANSPORT_URI, headers=HEADERS,data=PLAY_PAYLOAD%play_file)


if __name__ == "__main__":
   main(sys.argv[1])

