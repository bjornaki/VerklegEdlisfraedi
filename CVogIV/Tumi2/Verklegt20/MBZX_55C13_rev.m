fid1 = fopen('BZX-55C13_rev.txt');
if fid1 ~= -1
teljari_rev = 1;
Voltage_rev = [];
Current_rev = [];
Resistance_rev = [];
Power_rev = [];
Time_rev = [];
end
while ~feof(fid1)
line = fgetl(fid1);
k= str2num(line);
Voltage_rev(teljari_rev) = k(1);
Current_rev(teljari_rev)=k(2);
Resistance_rev(teljari_rev)=k(3);
teljari_rev = teljari_rev+1;
end
figure(1)
VoltageMBZX_55C13_rev=flip(-Voltage_rev);
CurrentMBZX_55C13_rev=flip(Current_rev);
plot(flip(-Voltage_rev),flip(Current_rev))
figure(2)
plot(VoltageMBZX_55C13_rev,log(CurrentMBZX_55C13_rev))