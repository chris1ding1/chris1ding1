# 使用随机端口（避免使用常见端口）
PORT=$((10000 + RANDOM % 50000))

# 添加流量混淆
sudo docker run -d --name gost \
    --restart=unless-stopped \
    -v ${CERT_DIR}:${CERT_DIR}:ro \
    --net=host \
    ginuerzh/gost \
    -L "http2://${USER}:${PASS}@${BIND_IP}:${PORT}?cert=${CERT}&key=${KEY}&probe_resist=code:404&knock=www.google.com&probe_resist_domain=${FAKE_SITE}&mux=true&websocket=true"
