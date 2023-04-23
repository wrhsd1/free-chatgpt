FROM --platform=$TARGETPLATFORM rust:alpine3.16 as builder

WORKDIR /usr/src

RUN USER=root cargo new chatgpt

RUN echo -e "[source.crates-io]\nreplace-with = 'rsproxy'\n[source.rsproxy]\nregistry = 'https://rsproxy.cn/crates.io-index'\n[source.rsproxy-sparse]\nregistry = 'sparse+https://rsproxy.cn/index/'\n[registries.rsproxy]\nindex = 'https://rsproxy.cn/crates.io-index'\n[net]\ngit-fetch-with-cli = true" ~/.cargo/config

COPY Cargo.toml Cargo.lock /usr/src/chatgpt/

WORKDIR /usr/src/chatgpt

RUN apk add musl-dev openssl openssl-dev pkgconfig 

RUN cargo build --release

COPY src /usr/src/chatgpt/src/

RUN RUST_BACKTRACE=1 cargo build  --release

FROM --platform=$TARGETPLATFORM alpine:3.16.0 AS runtime

WORKDIR /usr/local/chatgpt/

COPY --from=builder /usr/src/chatgpt/target/release/chatgpt /usr/local/chatgpt/

CMD ["/usr/local/chatgpt/chatgpt"]
