fid1 = fopen('1N4148_rev_3.txt');
if fid1 ~= -1
teljari = 1;
Voltage = [];
Current = [];
Resistance = [];
Power = [];
Time = [];
end
while ~feof(fid1)
line = fgetl(fid1);
k= str2num(line);
Voltage(teljari) = k(1);
Current(teljari)=k(2);
Resistance(teljari)=k(3);
teljari = teljari+1;
end
figure(1)
VoltageM1N4148_rev3=flip(-Voltage);
CurrentM1N4148_rev3=flip(Current);
plot(flip(-Voltage),flip(Current))
figure(2)
plot(VoltageM1N4148_rev3,log(CurrentM1N4148_rev3));