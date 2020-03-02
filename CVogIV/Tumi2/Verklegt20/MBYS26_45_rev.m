fid1 = fopen('BYS26-45_rev.txt');
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
VoltageBYS26_45_rev=flip(-Voltage);
CurrentBYS26_45_rev=flip(Current);
plot(flip(-Voltage),flip(Current))
figure(2)
plot(VoltageBYS26_45_rev,log(CurrentBYS26_45_rev));