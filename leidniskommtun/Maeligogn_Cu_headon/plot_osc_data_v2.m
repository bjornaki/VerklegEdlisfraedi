% Unnar Arnalds og Einar Baldur �orsteinsson
% Updated by Einar on 27 February 2020

% Góð mæligögn fyrir tímagraf
% 56, 57, 71, 83

V0 = 0.1014; % power supply voltage
R = 1000;    % Resistor value
Vz = -4e-4;  % offset voltage on the scope, often different between measurements
Iz = Vz/R;   % offset current calculated form the resistance

% Picking which datafiles to load
Number = 41:106;

% Picking which dataset to plot
PlotSelect = 56;

% Select which data to include in histogram
% Can be vector with the number of filenames
% HistSelect = [1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19, 21, 22, 24, 25]; 
HistSelect = Number; 

% Error checking that PlotSelect is a valid filename number
if PlotSelect < min(Number) || max(Number) < PlotSelect
    disp(' ')
    disp('Please check that PlotSelect is a valid filename number')
    disp(' ')
end

% Error checking that all HistSelect is a valid filename number
for i = 1:length(HistSelect)
    if  isempty(find(Number == HistSelect(i),1))
        disp(' ')
        disp('Please check that all HistSelect correspond to a valid filename number')
        disp(' ')
    end
end

%Preallocate
T = cell(1, length(Number));
VR = cell(1, length(Number));
I = cell(1, length(Number));
G = cell(1, length(Number));

% Load all datafiles
for i = 1:length(Number)
    filename = ['scope_' num2str(Number(i)) '.csv'];
    file = fopen(filename);
    Read = textscan(file, '%f %f %f', 'delimiter', ',','Headerlines', 2);
    fclose(file);
    %Extract the parameters from datafiles
    T{i} = Read{1};
    VR{i} = Read{2} - Vz;
    I{i} = (1/R)*VR{i}-Iz;
    G{i} = (VR{i}./R)./(V0-VR{i});
end

% Find which matlab vector number corresponds to the filename number
PS = find((Number == PlotSelect));

% Figure 1 is Current vs Time
figure(1)
clf
plot(T{PS}, I{PS});
set(gca,'FontName', 'helvetica', 'FontSize', 16);
xlabel('Time [s]');
ylabel('Current [A]');
title(['scope ' num2str(Number(PS)) ])
hold on
% Add expected lines
for n = 0:1:24
    In = (V0)/(R+(12.9E3/n));
    plot([min(T{PS}), max(T{PS})], [In,In]);
end
axis([min(T{PS}) max(T{PS}) -2e-6 8e-5])

% Plot using determined conductance values of the nanowire 2e^2/h
G0 = 7.7498e-5;

% Figure 2 is Conductance vs Time
figure(2)
clf
plot(T{PS}, G{PS}/G0, 'b', 'Linewidth',1);
set(gca,'FontName', 'helvetica', 'FontSize', 18)
xlabel('Time [s]');
ylabel('Conductance [2e^2/h]');
title(['scope ' num2str(Number(PS)) ])
hold on;
for n = 0:1:24
    plot([min(T{PS}), max(T{PS})], [n,n]);
end
axis([min(T{PS}) max(T{PS}) -1 20])


% Initialize
HS = [];
TOT = [];
TOT_G = [];

% Find which matlab vector number corresponds to the filename number
for i = 1:length(HistSelect)
    HS(i) = find((Number == HistSelect(i)));
end

% All Current and Conductance values appended together
for i = 1:length(HS)
    TOT = [TOT, I{HS(i)}];
    TOT_G = [TOT_G, G{HS(i)}];
end

%Select the bin width for the Current data
BW = 8E-7;

% Figure 3 is a histogram from the Current data
figure(3)
clf
histogram(TOT, 'BinWidth', BW, 'BinLimits', [-1e-5,1e-4]);
set(gca, 'FontName', 'helvetica', 'FontSize', 16)
xlabel('Current [A]');
ylabel('Occurrence [Counts]');
hold on
axis([-0.5e-5 5e-5 0 1000])
% Add expected lines
for n = 0:1:24
    I = (V0/R)/(1+(12.9E3/R)/n);
    plot([I, I], [0, 100], 'LineWidth', 2);
end



% Figure 4 is a histogram from the Conductance data
figure(4)
clf
histogram(TOT_G/G0, 'BinWidth', 0.1, 'BinLimits', [-1,12]);
set(gca, 'FontName', 'helvetica', 'FontSize', 16)
xlabel('Conductance [2e^2/h]');
ylabel('Occurrence [Counts]');
hold on
axis([-0.5 8 0 1000])
% Add expected lines
for n = 0:1:24
    plot([n n], [0, 100], 'LineWidth', 2);
end






