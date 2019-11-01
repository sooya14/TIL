// node === 기존의 입출력이 잘aht 일어나고 있었어서 c 로 만들어낸 환경 => 서버를 만들 수 있게 되었다. 

// 아래코드는 아무것도 없는 상태에서 서버 짠 것 

const http = require('http');
const port = 3001;

http.createServer((req, res) => {
    res.writeHead(200, {
        'Content-Type': 'text/plain',
    });
    res.statusCode = 200;
    res.end('End of response\n');
}).listen(port);

console.log(`Server is running @ http://loclahost:${port}`);