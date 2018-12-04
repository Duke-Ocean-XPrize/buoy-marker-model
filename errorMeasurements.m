% I have adhered to all the tenets of the
% Duke Community Standard in creating this code.
% Signed: [az73]

actualX = [0.0, 0.5, -0.5, 0.0, 0.0, 0.5];
actualY = [-0.5, -0.5, 0.15, 0.15, 0.15, 0.15];
actualZ = [3.0, 2.5, 2.0, 1.5, 1.0, 0.5];

measuredX = [0.2260003091465015, 0.539337805545108, -0.0955411711546724, ...
    0.25083453971433867, 0.23592277492994485, 0.3166804623961357];
measuredY = [-0.9036565855961202, -0.8656376205957353, -0.005805840002677583, ...
    -0.052328328076992794, -0.15777351438220122, -0.07653146246143244];
measuredZ = [3.293166920469143, 2.9812171184139036, 2.0236091821129403, ...
    1.7880688645290288, 1.221224215442547, 0.7478678143169196];

figure(1)
clf;
hold on;

xplot2 = plot(actualX, abs(measuredX - actualX), 'k+');
yplot = plot(actualY, abs(measuredY - actualY), 'kx');
zplot = plot(actualZ, abs(measuredZ - actualZ), 'ko');

xlabel('Actual Distances from Camera Axis in Meters');
ylabel('Absolute Difference of Measured vs. Actual Distance in Meters');
title('Absolute Difference (measured - actual) vs. Actual Distance for 100-point Averaged Measurements');
legend('X', 'Y', 'Z');

figure(2)
clf;

hold on;
D3plot1 = scatter3(measuredX, measuredZ, measuredY, 'filled');
text(measuredX(1)+0.05, measuredZ(1)+0.05, measuredY(1)+0.05, '1');
text(measuredX(2)+0.05, measuredZ(2)+0.05, measuredY(2)+0.05, '2');
text(measuredX(3)+0.05, measuredZ(3)+0.05, measuredY(3)+0.05, '3');
text(measuredX(4)+0.05, measuredZ(4)+0.05, measuredY(4)+0.05, '4');
text(measuredX(5)+0.05, measuredZ(5)+0.05, measuredY(5)+0.05, '5');
text(measuredX(6)+0.05, measuredZ(6)+0.05, measuredY(6)+0.05, '6');
D3plot2 = scatter3(actualX, actualZ, actualY, 'filled');
text(actualX(1)+0.05, actualZ(1)+0.05, actualY(1)+0.05, '1');
text(actualX(2)+0.05, actualZ(2)+0.05, actualY(2)+0.05, '2');
text(actualX(3)+0.05, actualZ(3)+0.05, actualY(3)+0.05, '3');
text(actualX(4)+0.05, actualZ(4)+0.05, actualY(4)+0.05, '4');
text(actualX(5)+0.05, actualZ(5)+0.05, actualY(5)+0.05, '5');
text(actualX(6)+0.05, actualZ(6)+0.05, actualY(6)+0.05, '6');
title('3D Scatter-Plot of Measured Distances (Blue) and Actual Distances (Orange) for T-Vec');
xlabel('X-Distance from camera (meters)');
ylabel('Z-Distance from camera (meters)');
zlabel('Y-Distance from camera (meters)');
grid on;
