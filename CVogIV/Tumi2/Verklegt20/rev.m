figure(1)
plot(VoltageMBZX_55C13_rev,CurrentMBZX_55C13_rev,'k',VoltageBYS26_45_rev,CurrentBYS26_45_rev,'m',VoltageBLED_rev,CurrentBLED_rev,'b',VoltageM1N4148_rev3,CurrentM1N4148_rev3,'r')
legend('BZX-55C13','BYS26-45','Blár ljómtvistur','1N4148', 'Location', 'NorthWest');
xlabel('Spenna (V)','fontsize',18);
ylabel('Straumur (A)');
figure(2)
semilogy(VoltageMBZX_55C13_rev,CurrentMBZX_55C13_rev,'k',VoltageBYS26_45_rev,CurrentBYS26_45_rev,'m',VoltageBLED_rev,CurrentBLED_rev,'b',VoltageM1N4148_rev3,CurrentM1N4148_rev3,'r')
legend('BZX-55C13','BYS26-45','Blár ljómtvistur','1N4148', 'Location', 'NorthWest');
xlabel('Spenna (V)');
ylabel('Straumur (A)');