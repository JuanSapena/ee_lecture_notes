% schematic plot of Markowitz's efficient frontier

sigma = 0:0.1:0.5;

mu_e = 0.03;
sigma_s = sqrt(mu_e);
mu_r = 0.05;

S = mu_e/sigma_s;
mu = mu_r + S*sigma;

figure(1)
clf

lw = 2; ms = 24; fs = 14; grey = 0.7*ones(1,3);

plot(sigma,mu,'-k','LineWidth',lw)
hold on

ds = 0.01; dm = -0.003;

plot(0,mu_r,'.r','MarkerSize',ms)
text(0+ds,mu_r+dm,'$(0, \mu_\mathrm{r})$','FontSize',fs)

plot(sigma_s,mu_r+mu_e,'.r','MarkerSize',ms)
text(sigma_s+ds,mu_r+mu_e+dm,'$(\sigma_\mathrm{s}, \mu_\mathrm{r}+\mu_\mathrm{e})$','FontSize',fs)

l = 1.5;
plot(l*sigma_s,mu_r+l*mu_e,'.b','MarkerSize',ms)
text(l*sigma_s+ds,mu_r+l*mu_e+dm,'$(\ell\sigma_\mathrm{s}, \mu_\mathrm{r}+\ell\mu_\mathrm{e})$','FontSize',fs)

plot([0.15,0.2,0.25,0.3,0.35,0.4],[0.055,0.06,0.055,0.065,0.08,0.075],'.','Color',grey,'MarkerSize',ms)

axis([0 sigma(end) 0.03 0.14])

xl = get(gca,'XLim');
yl = get(gca,'YLim');
base = [0.2,0.095];
tip = base + 0.1*[1,S];
xarrow = [(base(1)-xl(1))/(xl(2)-xl(1)), (tip(1)-xl(1))/(xl(2)-xl(1))];
yarrow = [(base(2)-yl(1))/(yl(2)-yl(1)), (tip(2)-yl(1))/(yl(2)-yl(1))];
annotation('textarrow',xarrow,yarrow,'String','$\ell\ $','FontSize',fs)

xlabel('volatility, $\sigma$','FontSize',fs)
ylabel('drift, $\mu$','FontSize',fs)
set(gca,'XTickLabel',[],'YTickLabel',[])

savepdf(gcf,'markowitz')