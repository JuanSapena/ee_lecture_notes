clf;
load('trajectories.mat');
% N=1;
% t=1040;
% r=rand(t,N);
% r(r>.5)=1.5;
% r(r<=.5)=.6;
% x=ones(t,N+1);
% for i=2:t
%     x(i,1)=i;
%     x(i,2:N+1)=x(i-1,2:N+1).*r(i,:);
% end
% x1=x(:,1:2);
stairs(x1(:,1),x1(:,2),'lineWidth', 3);
legend('N=1','location','northEast');
axis([0 1040 0 max(x1(1:1020,2))+1]);
xlabel('t');
ylabel('<x(t)>_N');
set(gca,'LooseInset',get(gca,'TightInset'))
saveas(gca,'./../figs/fig1_3a.pdf');

%...and on log-y scale
clf;
stairs(x1(:,1),x1(:,2),'lineWidth', 3);
set(gca, 'YScale', 'log')
legend('N=1','location','northEast');
axis([0 1040 min(x1(1:1040,2)) max(x1(1:1040,2))]);
xlabel('t');
ylabel('<x(t)>_N');
set(gca,'LooseInset',get(gca,'TightInset'))
saveas(gca,'./../figs/fig1_3b.pdf');
