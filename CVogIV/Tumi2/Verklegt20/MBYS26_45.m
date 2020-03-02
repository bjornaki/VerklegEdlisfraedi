fid1 = fopen('BYS26-45.txt');
if fid1 ~= -1
teljari = 1;
VoltageMBYS26 = [];
CurrentMBYS26 = [];
Resistance = [];
Power = [];
Time = [];
end
while ~feof(fid1)
line = fgetl(fid1);
k= str2num(line);
VoltageMBYS26(teljari) = k(1);
CurrentMBYS26(teljari)=k(2);
Resistance(teljari)=k(3);
teljari = teljari+1;
end
figure(1)
plot(VoltageMBYS26,CurrentMBYS26)
figure(2)
plot(VoltageMBYS26,log(CurrentMBYS26))
size(VoltageMBYS26);
hold on
%Línulegur hluti ferils nálgaður með jöfnu línu
VoltageMBYS26_lin=VoltageMBYS26(10:65);
lgCurrentMBYS26_lin=log(CurrentMBYS26(10:65));
pMBYS26=polyfit(VoltageMBYS26_lin,lgCurrentMBYS26_lin,1);
%Hallatala línu
h_MBYS26=real(pMBYS26(1));
%Lína plottuð með log-grafi
x=[0,0.35];
y=polyval(pMBYS26,x);
plot(x,y);
%Gæðastuðull
q_yfir_kbT=39.352;
gaediMBYS26=q_yfir_kbT/h_MBYS26