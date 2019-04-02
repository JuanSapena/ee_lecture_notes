% Whitworth III
% General lottery aka Peterbsurg Game

clear all

rounds = 1e3;
trials = 10;

t = 1:rounds;

w0 = 100;
price = 10;

wa = w0*ones(rounds,trials);
wm = wa;

x = 2.^ceil(-log2(rand(rounds,trials)));

for i = 2:rounds
    wm(i,:) = wm(i-1,:).*(w0 + x(i,:) - price)/w0; % multiplicative repetition
    wa(i,:) = wa(i-1,:) + x(i,:) - price; % additive repetition
end

figure(1), clf
plot(t,wa,'LineWidth',3)
xlabel('time / $\delta t$')
ylabel('wealth / $\pounds$')
savepdf(gcf,'lottery_add_traj')

figure(2), clf
plot(t,wm,'LineWidth',3)
set(gca,'YScale','log')
xlabel('time / $\delta t$')
ylabel('wealth / $\pounds$')
savepdf(gcf,'lottery_mult_traj')