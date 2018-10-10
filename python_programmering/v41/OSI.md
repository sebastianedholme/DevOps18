# TCP/IP & OSI MODELS #

TCP/IP modellen innehåller fyra lager medan OSI har 7 lager. Där lagrena är utbytbara med varandra. TCP/IP kan ses som en mindre modell av OSI. 

# TCP/IP Lager

- Applikationslager behandlar representation av data, kodning och kontroll. I OSI modellen består av 3 egna lager, Applikation, Presentation och session. 
- Host-to-Host lagret behandlar uppdelningen av applikations segmentering,hur pålitlig anslutningen är, flödet av data samt fel kontroller. Det är lagret är detsamma i OSI modellen.
- Internet lagret ser till att paket hamnar där det ska, oavsett vilken väg paketen tar. OSI lagret är densamma här också.
- Nätverks åtkomst lagret har hand om nätverkskortet och fysiska problem som uppstår när data överföring avbryts. I OSI modellen uppdelas de i Psychical(nätverkskortet) och Data Link som har hand om LAN och WAN.

Exempel på olika program/protokol osv som behandlar de olika lagrena är,

- Applikationslager, TFTP, TELNET, NFS, SMTP, DNS, rlogin, LDP, SNMP
- Host-to-Host, TCP, UDP (De olika internet protokollen)
- Internet ICMP, ARP, RARP, IP
- Network Access, Ethernet, Fast Ethernet, PPP, FDDI, ATM, Token Ring, Frame Relay, HDLC

# Host-to-Host protokollen TCP/UDP

## TCP 

TCP kräver en att en anslutning är giltig innan den skickar paket. De olika paketen delas upp segment. TCP protokollets uppgift är att dela upp en ström av och dela in de i segmenten, skicka om sånt som inte kom fram och organisera de strömmen i rätt ordning. MTU ställer in max storleken i byte för varje segment (1500 är max då det är max för ethernet payload size)

De viktiga segmenten är source port, destination port som tillsammans identifierar portar där anslutningen kan ske. Portarna plus en IP formar en anslutning som kan ha hand om data som lever i de högre lagrena.

Sequence Number och Acknoledgement Number segmenten specifierar bytes i byte strömmen. Det är med hjälp av de bytes som de olika segmenten kan identiferas av TCP protokollet. 

TCP Header length / Data offset, talar om hur många 4-byte ord som finns i TCP headern. 

Window segmentet indikerar hur många bytes som kan föras över innan en acknoledgement är skickas.

Checksum segmentet är extra lager för säkerhet och hjälper till att säkra att all data är intakt.

User Data segmentet innehåller all användar som skickas och ligger efter hela headern. 

## UDP 

UDP har inte alls lika många segment. Det finns inga krav på anslutningen, att datan är intakt eller inte när den når fram. UDP används när man snabbt behöver skicka data. Säkerheten som finns i TCP protokollet bör istället tas hand om i applikations lagret eller program som skickar / tar emot datan. 

Som i TCP finns Source / Destination port. Där portar som är öppna tillåter anslutning.

Sedan finns Length, Checksum och sist Data.

## Jämnförelser

TCP bör användas när det är viktigt att veta att en anslutning verkligen fungerar och är igår, när data är viktig och behöver säkerställas.

TCP är pålitligt, inte UDP
TCP kräver att anslutningen är bekräftad, inte UDP
TCP har windowing och att data som gått förlorad skickas igen, inte UDP
TCP Skickar segmenten i specifierad ordning, inte UDP
TCP Talar om att datan är mottagen, inte UDP.
