%FRW
fid1 = fopen('1N4148_frw.txt');
if fid1 ~= -1
teljari_frw = 1;
VoltageM1N4148 = [];
CurrentM1N4148 = [];
Resistance_frw = [];
Power_frw = [];
Time_frw = [];
end
while ~feof(fid1)
line = fgetl(fid1);
k= str2num(line);
VoltageM1N4148(teljari_frw) = k(1);
CurrentM1N4148(teljari_frw)=k(2);
Resistance_frw(teljari_frw)=k(3);
teljari_frw = teljari_frw+1;
end
figure(1)
plot(VoltageM1N4148,CurrentM1N4148);
figure(2)
plot(VoltageM1N4148,log(CurrentM1N4148));
size(VoltageM1N4148)
hold on
%Línulegur hluti ferils nálgaður með jöfnu línu
VoltageM1N4148_lin=VoltageM1N4148(50:60);
lgCurrentM1N4148_lin=log(CurrentM1N4148(50:60));
pM1N4148=polyfit(VoltageM1N4148_lin,lgCurrentM1N4148_lin,1);
%Hallatala línu
h_1N4148=real(pM1N4148(1));
%Lína plottuð með log-grafi
x=[0,1];
y=polyval(pM1N4148,x);
plot(x,y);
%Gæðastuðull
q_yfir_kbT=39.352;
gaedi1N4148=q_yfir_kbT/h_1N4148