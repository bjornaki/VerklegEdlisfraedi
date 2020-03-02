figure(1)
plot(VoltageMBYS26,CurrentMBYS26,'m',VoltageM1N4148,CurrentM1N4148,'r',VoltageMBZX,CurrentMBZX,'k',VoltageBLED,CurrentBLED,'b')
legend('BYS26','1N4148','BZX-55C13',  'Blár ljómtvistur', 'Location', 'NorthEast');
xlabel('Spenna (V)');
ylabel('Straumur (A)');
axis([0,4,-0.01,0.21]);
xticks([0 1 2 3 4])
yticks([0,0.05,0.1,0.15,0.2]);

figure(2)
semilogy(VoltageMBYS26,CurrentMBYS26,'m',VoltageM1N4148,CurrentM1N4148,'r',VoltageMBZX,CurrentMBZX,'k',VoltageBLED,CurrentBLED,'b')
legend('BYS26','1N4148','BZX-55C13',  'B-LED', 'Location', 'East');
xlabel('Spenna (V)');
ylabel('Straumur (A)');