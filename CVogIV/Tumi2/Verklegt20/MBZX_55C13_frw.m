%Gögn sótt
fid1 = fopen('BZX-55C13_frw.txt');
if fid1 ~= -1
teljari = 1;
VoltageMBZX = [];
CurrentMBZX = [];
Resistance = [];
Power = [];
Time = [];
end
while ~feof(fid1)
line = fgetl(fid1);
k= str2num(line);
VoltageMBZX(teljari) = k(1);
CurrentMBZX(teljari)=k(2);
Resistance(teljari)=k(3);
teljari = teljari+1;
end
%Straumur sem fall af spennu
figure(1)
plot(VoltageMBZX,CurrentMBZX)
%Log-straumur sem fall af spennu
figure(2)
plot(VoltageMBZX,log(CurrentMBZX))
hold on
%Línulegur hluti ferils nálgaður með jöfnu línu
VoltageMBZX_lin=VoltageMBZX(300:1000);
lgCurrentMBZX_lin=log(CurrentMBZX(300:1000));
pMBZX=polyfit(VoltageMBZX_lin,lgCurrentMBZX_lin,1)
%Hallatala línu
h_MBZX=real(pMBZX(1))
%Lína plottuð með log-grafi
x=[0.2,1];
y=polyval(pMBZX,x);
plot(x,y)
%Gaedastudull
q_yfir_kbT=39.352;
gaediMBZX=q_yfir_kbT/h_MBZX
