FROM mcr.microsoft.com/dotnet/sdk:9.0

WORKDIR /usr/app
COPY . .

RUN dotnet publish BillingService.csproj -c Release -o /usr/app/publish
RUN apt-get update \
    && apt-get install -y --no-install-recommends wget \
    && wget -O /tmp/gg.deb https://github.com/grft-dev/graftcode-gateway/releases/latest/download/gg_linux_amd64.deb \
    && dpkg -i /tmp/gg.deb \
    && rm /tmp/gg.deb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app/publish
EXPOSE 80
EXPOSE 81

CMD ["gg", "BillingService.dll"]
