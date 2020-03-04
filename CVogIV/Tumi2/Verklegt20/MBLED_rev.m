fid1 = fopen('BLED_rev.txt');
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
VoltageBLED_rev=flip(-Voltage(1:769));
CurrentBLED_rev=flip(Current(1:769));
plot(flip(-Voltage(1:769)),flip(Current(1:769)))
figure(2)
plot(VoltageBLED_rev,log(CurrentBLED_rev));