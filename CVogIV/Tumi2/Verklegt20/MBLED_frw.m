%Gögn sótt
fid1 = fopen('BLED_frw.txt');
if fid1 ~= -1
teljari = 1;
VoltageBLED = [];
CurrentBLED = [];
Resistance = [];
Power = [];
Time = [];
end
while ~feof(fid1)
line = fgetl(fid1);
k= str2num(line);
VoltageBLED(teljari) = k(1);
CurrentBLED(teljari)=k(2);
Resistance(teljari)=k(3);
teljari = teljari+1;
end
%Straumur sem fall af spennu
figure(1)
plot(VoltageBLED,CurrentBLED)
%log-straumur sem fall af spennu
figure(2)
plot(VoltageBLED,log(CurrentBLED))
size(VoltageBLED)
hold on
%Línulegur hluti ferils nálgaður með jöfnu línu
VoltageBLED_lin=VoltageBLED(240:241);
lgCurrentBLED_lin=log(CurrentBLED(240:241));
pBLED=polyfit(VoltageBLED_lin,lgCurrentBLED_lin,1);
%Hallatala línu
h_BLED=real(pBLED(1));
%Lína plottuð með log-grafi
x=[1.0,3.5];
y=polyval(pBLED,x);
plot(x,y);
%Gæðastuðull
q_yfir_kbT=39.352;
gaediBLED=q_yfir_kbT/h_BLED
%Stór óvissa á gæðastuðli