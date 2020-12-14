yt = 20;  % Set-Point
Kp = 10;  % Proportional gain
Kd = 25; % Derivative gain
tStep = 0.01; % Step Time in seconds
TSim = 10; % Simulation time in seconds
T = 2; % Coeffecient of first order system

syms y(t)
ode = (T+Kd)*diff(y,t) + (1 + Kp)*y - yt*Kp;
initialCondition = y(0) == 0;
ySol(t) = dsolve(ode,initialCondition);
ySol = simplify(ySol);

simLength = length(0:tStep:TSim);
y = zeros(1,simLength);
x = zeros(1,simLength);

indexVar = 1;
for i=0:tStep:TSim
    x(indexVar) = i;
    y(indexVar) = ySol(i);
    indexVar = indexVar + 1;
end

disp(y(end));
plot(x,y);
